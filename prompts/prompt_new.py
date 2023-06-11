# this prompt is heavily inspired by the prompt used in:
# https://openaipublic.blob.core.windows.net/neuron-explainer/paper/index.html

prompt_start = """

We're studying clusters of neurons in a neural network. Each cluster looks for some particular thing in a short document. Look at the parts of the document the cluster activates for and summarize in a single sentence what the neuron is looking for. Don't list examples of words. Don't give overly broad explanations like "a number of tokens" or "specific tokens".
They can be context sensitive (where they depend on the preceding tokens or the placement in the text), content sensitive, or both (X content, but only in Y context).

The activation format is token<tab>activation. Activation values range from 0 to 10. A neuron finding what it's looking for is represented by a non-zero activation value. The higher the activation value, the stronger the match.
"""

prompt_end = "The main thing this cluster does is find"