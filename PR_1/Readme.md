# Practical No. 1: 


## Problem Statement
Perform tokenization (Whitespace, Punctuation-based, Treebank, Tweet, MWE) using nltk library. Use porter stemmer and snowball stemmer for stemming. Use any technique for lemmatization. Input / Dataset –use any sample sentence


## Explanation
In this practical, I have taken a sample sentence and applied different tokenization techniques on it. 

First, I used simple whitespace splitting to break the sentence. Then I used NLTK’s word_tokenize function which handles punctuation properly. I also used Treebank tokenizer and Tweet tokenizer to see how different tokenizers behave.

For multi-word expressions, I used MWETokenizer where phrases like "New York" and "machine learning" are treated as single tokens.

After that, I performed stemming using Porter and Snowball stemmers to reduce words to their root form. Finally, I used WordNet Lemmatizer to convert words into their proper base form.

## Output
The output shows how the text is split using different tokenization techniques and how words are changed after stemming and lemmatization.

## Conclusion
From this practical, I understood how important preprocessing is in NLP. Different methods give slightly different results, and these steps help in better text analysis later.