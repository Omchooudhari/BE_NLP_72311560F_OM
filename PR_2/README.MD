# Practical No. 2: 


## Problem Statement
Perform bag-of-words approach (count occurrence, normalized count occurrence), tf-idf on data.
Create embeddings using Word2Vec. Dataset to be used: https://www.kaggle.com/datasets/CooperUnion/cardataset


## Explanation
In this practical, I used a dataset and combined different columns like Make, Model, Engine Fuel Type, and Vehicle Style to create text data.

First, I applied TF-IDF using sklearn library. It helps to find important words in the text based on their frequency.

Then, I used Word2Vec from gensim to convert words into vectors based on their context. This helps in understanding the relationship between words.

I also checked similar words and created a sentence embedding by averaging word vectors.


## Output
The output shows TF-IDF features and matrix values, word vectors from Word2Vec, similar words, and sentence embedding.


## Conclusion
From this practical, I understood how text is converted into numerical format. These techniques are useful for machine learning and NLP tasks.