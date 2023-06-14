# Document for tests of methods from automatized Explain
import unittest
import automatized_explain
import prompts

class TestExplainerMethods(unittest.TestCase):
	#explainer = automatized_explain.Explainer(nmf_object)
#	Explainer
#	def setUpClass(cls):
#		@classmethod
#		cls._explainer = createExplainer()
	

	# need to explicitly pass components
	# Need to figure out how to correct for 
#	def test_normalize_components(self):
#		input = [[0, 0.5, 1],[1, 0.5, 0]]
#		expected = [[0, 5, 10], [10, 5, 0]]
#		result = automatized_explain.Explainer.normalize_components('', input)
#		# need to figure out how to compare lists of lists, 
#		# it seems like assertEqual only compares strings
#		self.assertEqual(result, expected)

	def test_create_new_result_string(self):
		# takes a minimum of 2 components
		input_components = [[0, 5, 10],[10, 5, 0]]
		input_tokens = ['test1', 'test2', 'test3']

		expected1 = '''Factor 1:\nActivations\n<start>\ntest1\t0\ntest2\t5\ntest3\t10\n<end>
same string but with all zeros filtered out:\n\n<start>\ntest2\t5\ntest3\t10\n<end>\n'''
		expected2 = '''Factor 2:\nActivations\n<start>\ntest1\t10\ntest2\t5\ntest3\t0\n<end>
same string but with all zeros filtered out:\n\n<start>\ntest1\t10\ntest2\t5\n<end>\n'''

		results = automatized_explain.Explainer.create_new_result_string('', input_components, input_tokens)
		result1 = results[0]
		result2 = results[1]

		self.assertEqual(result1, expected1)
		self.assertEqual(result2, expected2)
	
	def test_create_prompt(self):
		result_string = '''Factor 1:\nActivations\n<start>\ntest1\t0\ntest2\t5\ntest3\t10\n<end>
same string but with all zeros filtered out:\n\n<start>\ntest2\t5\ntest3\t10\n<end>\n'''

		result = automatized_explain.Explainer.create_prompt('', result_string)
		expected = ''

		self.assertEqual(result, expected)



if __name__ == '__main__':
	unittest.main()