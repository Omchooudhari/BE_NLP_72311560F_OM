import nltk
from nltk.tokenize import word_tokenize, TweetTokenizer, MWETokenizer
from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk.stem import PorterStemmer, SnowballStemmer
from nltk.stem import WordNetLemmatizer

# sample text
text = "Hello! I am learning NLP. This is a great experience :) #AI"

# whitespace
print("Whitespace:", text.split())

# punctuation (nltk)
print("Punctuation:", word_tokenize(text))

# treebank
tb = TreebankWordTokenizer()
print("Treebank:", tb.tokenize(text))

# tweet
tw = TweetTokenizer()
print("Tweet:", tw.tokenize(text))

# mwe
mwe = MWETokenizer([('New', 'York'), ('machine', 'learning')])
text2 = "I live in New York and love machine learning"
print("MWE:", mwe.tokenize(text2.split()))

# stemming
words = word_tokenize(text)

ps = PorterStemmer()
print("Porter:", [ps.stem(w) for w in words])

ss = SnowballStemmer("english")
print("Snowball:", [ss.stem(w) for w in words])

# lemmatization
lem = WordNetLemmatizer()
print("Lemma:", [lem.lemmatize(w) for w in words])