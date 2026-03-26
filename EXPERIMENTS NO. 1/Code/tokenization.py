import nltk
from nltk.tokenize import word_tokenize, TweetTokenizer, MWETokenizer
from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk.stem import PorterStemmer, SnowballStemmer
from nltk.stem import WordNetLemmatizer

# run once
nltk.download('punkt')
nltk.download('wordnet')

# input
text = "Hello! I am learning NLP. This is a great experience :) #AI"

print("\n================================ NLP TOKENIZATION OUTPUT ================================")

# whitespace
print("\n--- Whitespace Tokenization ---")
print("Whitespace:", text.split())

# punctuation (nltk)
print("\n--- Punctuation Tokenization ---")
print("Punctuation:", word_tokenize(text))

# treebank
tb = TreebankWordTokenizer()
print("\n--- Treebank Tokenization ---")
print("Treebank:", tb.tokenize(text))

# tweet
tw = TweetTokenizer()               # tweet tokenizer (handles hashtags, emojis,....)
print("\n--- Tweet Tokenization ---")
print("Tweet:", tw.tokenize(text))

# mwe
mwe = MWETokenizer([('New', 'York'), ('machine', 'learning')])      # treating 'New York' and 'machine learning' as single tokens
text2 = "I live in New York and love machine learning"
print("\n--- MWE Tokenization ---")
print("MWE:", mwe.tokenize(text2.split()))


words = word_tokenize(text)

# porter stemming 
ps = PorterStemmer()
print("\n--- Porter Stemming ---")
print("Porter:", [ps.stem(w) for w in words])

# snowball stemming 
ss = SnowballStemmer("english")
print("\n--- Snowball Stemming ---")
print("Snowball:", [ss.stem(w) for w in words])

# lemmatization 
lem = WordNetLemmatizer()
print("\n--- Lemmatization ---")
print("Lemma:", [lem.lemmatize(w) for w in words])