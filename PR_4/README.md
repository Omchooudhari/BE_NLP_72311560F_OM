# Practical No. 4: Transformer From Scratch using PyTorch


## Problem Statement
Create a transformer from scratch using the PyTorch library.


## Explanation
In this practical, I built a small transformer model from scratch using PyTorch.

I started by creating the self-attention part. It turns the input into query, key, and value vectors, then calculates attention scores and uses softmax to decide which tokens should matter more.

After that, I wrapped the attention layer inside a transformer block. This block adds residual connections and layer normalization, which help the model train more smoothly.

Then I combined everything into a simple transformer model with an embedding layer at the beginning and a linear layer at the end. The embedding layer converts token IDs into vectors, and the final layer maps the output back to the vocabulary size.

To check if it worked, I passed a random batch through the model. It returned the expected output shape, so the forward pass was working correctly.


## Output
The model printed the output tensor shape, which confirmed that everything ran as expected.


## Conclusion
This practical helped me understand how a transformer is built step by step in PyTorch and how self-attention, embeddings, and residual connections fit together.