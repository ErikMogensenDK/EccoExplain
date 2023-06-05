# EccoExplain
Addition of .explain() method to Ecco library's non-negative matrix factorization (NNMF) analysis tool.
By masking the tokens related to factors found using NNMF and feeding these to GPT-3.5, .explain() provides automatic explanations of what clusters of neurons might be responding to.

You can check out 2 examples of how it works in the "Notebook_to_publish.html" File.

If you want to use it, download Ecco from https://github.com/jalammar/ecco/, replace your output.py file with the one in this repository (or just add the .explain() method), and add the automatized_explain.py and embedding_searcher.py files, as well as the prompt and pkl files to your local ecco folder.
