# Practical 3: Text Preprocessing and TF-IDF

## Problem Statement
Perform text cleaning, perform lemmatization (any method), remove stop words (any method), label encoding. Create representations using TF-IDF. Save outputs. Dataset: https://github.com/PICT-NLP/BE-NLP-Elective/blob/main/3- Preprocessing/News_dataset.pickle



## Explanation
In this practical, I worked on a news dataset and applied different preprocessing steps to prepare the text for analysis.

First, I cleaned the text by converting it to lowercase and removing unwanted characters like numbers and symbols. This helps in making the text uniform.

Then, I performed tokenization and removed stopwords using NLTK. Stopwords are common words like "is", "the", "and" which do not add that much meaning.

After that, I applied lemmatization to convert words into their base form. This helps in reducing variations of the same word.

Next, I used LabelEncoder to convert the text labels into numerical form so that they can be used in ML models.

Finally, I applied TF-IDF using sklearn to convert the processed text into numerical vectors. This helps in identifying important words in each document.


## Output
The output shows cleaned text, tokenized words, lemmatized words, encoded labels, and TF-IDF representation. The processed dataset is also saved for further use.


## Conclusion
From this practical, I understood how raw text is cleaned and prepared before applying ML techniques. Preprocessing is an important step in NLP as it improves the quality of the data.