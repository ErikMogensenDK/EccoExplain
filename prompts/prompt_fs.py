# This prompt provides the context for the summarization of the non-negative matrix factorizations
prompt_start = """
You will act as an explainability module, providing a narrative explanation the relationship between several strings containing words.
You will receive several strings of initial text, but with masks.
A masked token is marked by 1 underscore.
Several underscores mean that several tokens have been replaced.
The tokens, which have not been replaced by an underscore, has been shown to be activated by some cluster of neurons of the large language model, in response to the input shown earlier.
Your job is to describe any relationship which might be present between the remaining tokens, which are not replaced by underscores.
These relationships might be syntactic, grammatic, semantic or some special token of the large language model like "[CLS]" and "[SEP]".
Just saying that "this factor relates to words" is insufficient. You must figure out what these tokens have in common.
They might attend to particular parts of a sentence like the start, middle or the end.
If there is no clear relationship between any of the tokens of a factor you should write: "No intuitive connection between the tokens of this factor was found.". 
Be brief, and only give a few examples.
You are to provide the "output" similiar to those in the examples. 
It's crucial that you DO NOT copy the most similiar example, but critically use them to the extent that they are similiar.
Please note, if only tokens from the beginning, middle or ending of a sequence are represented.
When you are providing your explanation of what the tokens have in common, you should ONLY use the masked string. Act as if you don't even know the original string.
"""
prompt_end = "Now it's your turn, continue using this input: "