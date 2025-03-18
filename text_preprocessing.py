# import necessary libraries
import nltk    # imports the nlp toolkit/library
from nltk.tokenize import word_tokenize, sent_tokenize    # imports the word_tokenize function

# dowunload necessary resources
nltk.download('punkt')   #this is done only once

# sample text to process
text = "Hello there! This is my first NLP project. " \
"Let's clean and process this text. We hope to learn something new today."


# 1. APPLYING TOKENIZATION

# break the text into sentences tokens
sentence = sent_tokenize(text)

# break the text into word tokens
words = word_tokenize(text)

# print them out
print('Sentences:', sentence)
print('Words:', words)


# 2. APPLYING STOPWORDS

from nltk.corpus import stopwords  # this imports the stopwords list

# download all the stopwords
nltk.download('stopwords')         # this is done only once too

# get only the list of english stopwords
stop_words = set(stopwords.words('english'))

# remove stopwords from the text
stop_words_removed = [word for word in words if word.lower() not in stop_words]


# 3. APPLYING STEMMING

from nltk.stem import PorterStemmer        # imports the PorterStemmer class

#instantiate the stemmer object
stemmer = PorterStemmer()

# applying stemming to the filtered words
stemmed_tokens = [stemmer.stem(word) for word in stop_words_removed]
