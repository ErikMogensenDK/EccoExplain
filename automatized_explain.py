import numpy as np
from ecco.prompts import prompt_fs
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
		prompt_for_gpt = prompt_fs.prompt_start.strip()
		searcher = Searcher(string_result, api_key=self.api_key)
		prompt_for_gpt = prompt_for_gpt + searcher.add_examples_to_prompt()
		prompt_for_gpt = prompt_for_gpt + prompt_fs.prompt_end.strip()
		prompt_for_gpt = prompt_for_gpt + string_result
		return prompt_for_gpt
	

	def get_response(self, prompt):
		# gets response in text using GPT 3.5 based model text-davinci-003
		response = (openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0.7, max_tokens=600))["choices"][0]["text"]
		return response

	def analyze(self):
		result_string_list = self.create_string_results_list(self.create_masked_token_lists(self.mask_elements_below_threshold()))
		factor_explanations = []
		for i in range(len(result_string_list)):
			prompt = self.create_prompt(result_string_list[i])
			response = self.get_response(prompt)
			factor_explanations.append(response)
		return factor_explanations

	
	#todos:
	#TODO check if model is ok and throw
	#TODO make sure text input isn't too long
	#TODO make api-call to openai try/except like, in case of unreliability/no internet
	#TODO include as many examples as you have space for.
	#TODO Figure out how to use 'gpt-3.5-turbo' instead, since it's 1/10 the price of davinci.

