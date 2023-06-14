# Small module created to index into vectors, containing explanations of Non-negative matrix factorizations

# Adapted from https://github.com/openai/openai-cookbook/blob/main/examples/Question_answering_using_embeddings.ipynb
import ast  # for converting embeddings saved as strings back to arrays
import openai  # for calling the OpenAI API
import pandas as pd  # for storing text and embeddings data
import tiktoken  # for counting tokens
from scipy import spatial  # for calculating vector similarities for search
import pickle

from prompts import prompt_new
class Searcher:
	def __init__(self, input_prompt, api_key = 'API_KEY', pkl_savepath = "C:/Users/erikm/dropbox/openai_like_explanations.pkl", MAX_TOKENS=3000):
		openai.api_key = api_key
		self.input_prompt = input_prompt
		#if CSV is preferred, commented out code is below:
		#self.examples_df = pd.read_csv(examples_csv_path)
		self.MAX_TOKENS = MAX_TOKENS
		self.prompt_start = prompt_new.prompt_start.strip()
		self.prompt_end = prompt_new.prompt_end.strip()
		with open(pkl_savepath, 'rb') as f:
			self.examples_df = pickle.load(f)

	def num_tokens(self, text: str) -> int:
		# encode string in tokens and return length of tokenized string
		model = "text-davinci-003"  # only matters insofar as it selects which tokenizer to use
		encoding = tiktoken.encoding_for_model(model)
		return len(encoding.encode(text))

	def get_examples_ranked_by_relatedness(self, relatedness_fn=lambda x, y: 1 - spatial.distance.cosine(x, y), top_n: int = 10):
		"""Returns a list of strings and relatednesses, sorted from most related to least."""
		query_embedding_response = openai.Embedding.create(
		    model="text-embedding-ada-002", #OpenAI's best embeddings as of Apr 2023
		    input=self.input_prompt,
		)
		query_embedding = query_embedding_response["data"][0]["embedding"]
		strings_and_relatednesses = [
		    (row["text"], relatedness_fn(query_embedding, row["embedding"]))
		    for i, row in self.examples_df.iterrows()
		]
		strings_and_relatednesses.sort(key=lambda x: x[1], reverse=True)
		strings, relatednesses = zip(*strings_and_relatednesses)
		return strings[:top_n]

	def add_examples_to_prompt(self):
		explanations = self.get_examples_ranked_by_relatedness()
		prompt = self.input_prompt
		current_length = self.num_tokens(prompt) + self.num_tokens(self.prompt_start) + self.num_tokens(self.prompt_end)
		for i in range(len(explanations)):
			length_of_string = self.num_tokens(explanations[i])
			if (current_length + length_of_string) <= self.MAX_TOKENS:
				prompt = prompt + explanations[i]
				current_length = current_length + length_of_string
			else:
				continue
		return prompt

#class Embedder(self, ):
