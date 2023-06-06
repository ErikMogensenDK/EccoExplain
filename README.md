# EccoExplain
Addition of .explain() method to Ecco library's non-negative matrix factorization (NNMF) analysis tool.
By masking the tokens related to factors found using NNMF and feeding these to GPT-3.5, .explain() provides automatic explanations of what clusters of neurons might be responding to.

You can check out 2 examples of how it works in the "Notebook_to_publish.html" File.

Interesting next steps could be to:
- Get the explaining model produce a few explanations, and to assess these explanations and pick the best ones - This might draw inspiration from the approach of "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" by Wei et, a. 2023.
- Get the explaining model to prove itself wrong, by providing the initial explanation and the input used to generate it. This might be inspired by an approach like in "Self-critiquing models for assisting human evaluators" by Saunders et, al. 2023 

If you want to use it, download Ecco from https://github.com/jalammar/ecco/, replace your output.py file with the one in this repository (or just add the .explain() method to your output.py file), and add the automatized_explain.py and embedding_searcher.py files, as well as the prompt and pkl files to your local ecco folder.
You will also need to setup an openai account.
