This repository provides a small extension to the Ecco library (https://github.com/jalammar/ecco/), consisting of a .explain() method for the non-negative matrix factorization - providing automated analysis of the tokens making up each factor.

The changes consist of:
An addition of an .explain() method to the nmf-class, which can be found in the output.py file!
This workings of the .explain() method are found in automatized_explain.py (which handles the masking of the tokens) and in embedding searcher
Additionally, the explain method uses 2 files: A pickle file containing the example explanations and their embeddings, and a prompt.py file containing the start and end of the prompt (which is read by automatized_explain).
The how to create the index of embedded explanations is walked through in the nmf_explanations_embeddings.ipynb notebook.
