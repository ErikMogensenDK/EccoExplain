# unittests for embedding_searcher
import unittest
import embedding_searcher
import prompts

class TestSearcherMethods(unittest.TestCase):

	def test_num_tokens(self):
		test_string = "testcase 1, for davinci-003 model"
		result = embedding_searcher.Searcher.num_tokens('', test_string)
		# insert actual number of tokens below:
		expected = 'x'
		self.AssertEquals(result, expected)
		
	#def test_get_examples_ranked_by_relatedness(self):
		# create test_df?
		# load test_def and pass it into get_examples method instead of using self.examples_df?

	#def test_add_examples_to_prompt(self):
		# currently depends on "get examples"
		# maybe examples should be passed as arguements instead of generated within the method



if __name__ == '__main__':
	unittest.main()