import openai
import numpy as np
from prompts import prompt_fs

class Explainer:
	def __init__(self, nmf_object, threshold = 0.1, api_key = "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"):
		openai.api_key = api_key
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

	def create_string_result(self, masked_strings):
		result_string = "The original string input was: '"
		original_input = "".join(self.tokens)
		n_of_factors = len(masked_strings)
		result_string = result_string + original_input + "'. \n"
		#result_string = result_string + f"The activations used to mask tokens was found with a threshold of {threshold}. \n"
		result_string = result_string + f"The activations were decomposed into {n_of_factors} factors. \n"
		#result_string = result_string + "Any mask is marked by replacing the original text with an underscore: '_' "
		for i in range(len(masked_strings)):
			string_to_add = f"Factor number {i+1} contained these tokens: '"
			#masked_string = "".join(masked_strings[i][1])
			# changed since create_Maskedd_token_lists no longer returns "words" AND "masked lists"
			masked_string = "".join(masked_strings[i])
			string_to_add = string_to_add + masked_string + "'. \n"
			result_string = result_string + string_to_add
		return result_string

	def create_prompt(self, string_result):
		prompt_for_gpt = prompt_fs.prompt.strip()
		prompt_for_gpt = prompt_for_gpt + string_result
		print("Prompt for gpt:")
		print(prompt_for_gpt)
		return prompt_for_gpt

	def get_response(self, prompt):
		# gets response in text using GPT 3.5 based model text-davinci-003
		#response = (openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0.5, max_tokens=600))["choices"][0]["text"]
		response = "test response, just to save money you know"
		return response

	def analyze(self):
		result_string = self.create_string_result(self.create_masked_token_lists(self.mask_elements_below_threshold()))
		prompt = self.create_prompt(result_string)
		response = self.get_response(prompt)
		return response

	
	#todo:
	#TODO check if model is ok
	#TODO make sure text input isn't too long
	#TODO make api-call to openai try/except like, in case of unreliability/no internet
	#TODO create Index (vector space of embeddings) with explanations!