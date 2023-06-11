import numpy as np
from ecco.prompts import prompt_new
import openai
import pandas as pd
from ecco.embedding_searcher import Searcher

class Explainer:
	def __init__(self, nmf_object, threshold = 0.01, api_key = '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' , example_csv_save_path = "C:/Users/erikm/dropbox/explanations.csv"):
		openai.api_key = api_key
		self.api_key = api_key
		self.components = nmf_object.components 
		self.tokens = nmf_object.tokens[0]
		self.num_of_tokens = len(nmf_object.tokens[0])
		self.threshold = threshold


#	def normalize_components(self):
#		range_val = np.ptp(self.components)
#		min_val = np.min(self.components)
#		# nested list comprehension, which normalizes all values between 0 and 1,
#		# multiplies value by 10 and rounds to nearest int.
#		normalized_components = [
#			np.around([
#				int(((x - min_val) / range_val) * 10)
#				for x in component
#			])
#			for component in self.components
#		]
#		return normalized_components

# new normalize component, which uses the range/minimum of each factor, rather than the min/range of all factors:
	def normalize_components(self):
		range_vals = [np.ptp(component) for component in self.components]
		min_vals = [np.min(component) for component in self.components]
		# nested list comprehension, which normalizes all values between 0 and 1,
		# multiplies value by 10 and rounds to nearest int.
		normalized_components = [
			np.around([
				int(((x - min_vals[i]) / range_vals[i]) * 10)
				for x in self.components[i]
			])
			for i in range(len(self.components))
		]
		return normalized_components
# new above

	def create_new_result_string(self, normalized_components):
		new_strings = []
		factor_count = 1
		for component in normalized_components:
			new_string = f'Factor {factor_count}:\nActivations\n<start>\n\n'
			for i in range(len(component)):
				new_string = new_string + f'{self.tokens[i]}\t{component[i]}\n'
			new_string = new_string + '<end>\n'

			new_string = new_string + f'same_string but with all zeros filtered out:\n\n<start>'	
			for i in range(len(component)):
				if component[i]>0:
					new_string = new_string + f'{self.tokens[i]}\t{component[i]}\n'
			new_string = new_string +'<end>\n'

			#print(new_string)

			new_strings.append(new_string)
			factor_count += 1
		return new_strings
	

	def mask_elements_below_threshold(self):
		masked_array = np.array([[0 if y < self.threshold else y for y in self.components[x]] for x in range(len(self.components))])
		return masked_array

	def create_masked_token_list(self, masked_activations):
		list_of_masked_tokens = [self.tokens[x] if masked_activations[x] != 0 else "_" for x in range(self.num_of_tokens)]
		return list_of_masked_tokens

	def create_masked_token_lists(self, masked_activations):
		masked_lists = [self.create_masked_token_list(masked_activations[x]) for x in range(len(masked_activations))]
		return masked_lists


	def create_string_result(self, masked_string):
		result_string =f"""threshold: {self.threshold}
n_components: {len(self.components)}
Original input string: {" ".join(self.tokens)}
Masked string: {" ".join(masked_string)}
Output: """
		return result_string

	def create_string_results_list(self, masked_strings_list):
		#iterate through list and create a string for each masked token
		result = [self.create_string_result(x) for x in masked_strings_list]
		return result

	def create_prompt(self, string_result):
		prompt_for_gpt = prompt_new.prompt_start.strip()
		searcher = Searcher(string_result, api_key=self.api_key)
		prompt_for_gpt = prompt_for_gpt + searcher.add_examples_to_prompt()
		prompt_for_gpt = prompt_for_gpt + string_result
		prompt_for_gpt = prompt_for_gpt + prompt_new.prompt_end.strip()
		return prompt_for_gpt
	

	def get_response(self, prompt):
		# gets response in text using GPT 3.5 based model text-davinci-003
		response = (openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0.7, max_tokens=600))["choices"][0]["text"]
		#response = "Test response"
		return response

	def analyze(self):
		#result_string_list = self.create_string_results_list(self.create_masked_token_lists(self.mask_elements_below_threshold()))
		result_string_list = self.create_new_result_string(self.normalize_components())
		factor_explanations = []
		for i in range(len(result_string_list)):
			prompt = self.create_prompt(result_string_list[i])
			response = self.get_response(prompt)
			print(result_string_list[i] + 'Explanation of Factor: the main thing this cluster of neurons does is find' + response)
			factor_explanations.append(response)
		return factor_explanations

	
	#todos:
	#TODO check if model is ok and throw
	#TODO make sure text input isn't too long
	#TODO make api-call to openai try/except like, in case of unreliability/no internet
	#TODO include as many examples as you have space for.
	#TODO Figure out how to use 'gpt-3.5-turbo' instead, since it's 1/10 the price of davinci.
	#TODO write tests for the different methods

	# Instead write: Word: Activation
	# for every word in the sequence
	# OR You can place ** around every word...

