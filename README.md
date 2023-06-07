# EccoExplain
Addition of .explain() method to Ecco library's non-negative matrix factorization (NMF) analysis tool.
By masking the tokens related to factors found using NMF and feeding these to GPT-3.5, .explain() provides automatic explanations of what clusters of neurons might be responding to.
Openai has recently build automatic explanation of individual neurons: https://openaipublic.blob.core.windows.net/neuron-explainer/paper/index.html.
This approach does, however, not address polysemanticism of neurons, and this approach also struggles to automatically account for context-related activation (like neurons firing after misspelled words).
They point to NMF as a potential next step.

You can check out 2 examples of how it works in the "Notebook_to_publish.html" File.

Interesting next steps could be to:
- Get the explaining model produce a few explanations, and to assess these explanations and pick the best ones
- Get the explaining model to prove itself wrong, by providing the initial explanation and the input used to generate it. 
These ideas are inspired by the approach in "Self-critiquing models for assisting human evaluators" by Saunders et, al. 2023 

Additionally it would be interesting to investigate how well the cluster of activations generalizes to other contexts:
- Does the "middle of the sentence" cluster only activate on longer sequences?
- Is the "period" cluster activated both when used in text, and when used in code?

If you want to use it, download Ecco from https://github.com/jalammar/ecco/, replace your output.py file with the one in this repository (or just add the .explain() method to your output.py file), and add the automatized_explain.py and embedding_searcher.py files, as well as the prompt and pkl files to your local ecco folder.
You will also need to setup an openai account.
