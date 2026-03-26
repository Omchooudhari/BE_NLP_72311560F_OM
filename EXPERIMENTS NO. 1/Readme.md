# Experiment No. 1: 

## Problem Statement
Perform tokenization (Whitespace, Punctuation-based, Treebank, Tweet, MWE) using nltk library. Use porter stemmer and snowball stemmer for stemming. Use any technique for lemmatization. Input / Dataset –use any sample sentence


## Explanation
In this experiment, I used a sample sentence to understand different NLP preprocessing techniques. 

First, I performed whitespace tokenization by simply splitting the sentence. Then I used NLTK’s word_tokenize function for punctuation-based tokenization. I also implemented Treebank tokenizer and Tweet tokenizer to see how they handle text differently.

For multi-word expressions, I used MWETokenizer where phrases like "New York" and "machine learning" are treated as single tokens.

After tokenization, I applied stemming using Porter and Snowball stemmers to reduce words to their root form. Finally, I used WordNet Lemmatizer to get the proper base form of words.


## Output
The output shows how the input sentence is tokenized using different techniques and how words are transformed using stemming and lemmatization.


## Conclusion
Through this experiment, I understood the importance of text preprocessing in NLP. Different tokenization methods give different results, and stemming and lemmatization help in reducing words to their base form which is useful for further text analysis.