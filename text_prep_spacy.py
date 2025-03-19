import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load the small English model in spaCy
nlp = spacy.load("en_core_web_sm")

# Define your text
text = "Machine learning is transforming the world of data science. It helps in making accurate predictions and decisions."

# Step 1: Remove stop words using NLTK
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(text)
filtered_text = ' '.join([word for word in word_tokens if word.lower() not in stop_words])

print("Filtered Text (After NLTK Stop Word Removal):", filtered_text)

# Step 2: Process the filtered text using spaCy
doc = nlp(filtered_text)

# sentence tokenize
for sent in doc.sents:
  print(sent)

# word tokenize
for  word in doc.text:
  print(word)

# apply lemmatization and placing the words side by side
for token in doc:
  print(token.text, '|', token.lemma_)