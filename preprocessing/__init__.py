import re
import nltk

stopwords = nltk.corpus.stopwords.words('portuguese')

# import spacy
# nlp = spacy.load('pt')

def lemmatize(text):
    global tokens
    tokens = nlp(text)
    lemmas = [token.lemma_ for token in tokens]
    return ' '.join(lemmas)

def cleanText(text):
    text = re.sub(r'[0-9"\(\)\,\:]+', ' ', text)
    text = re.sub(r'[\n ]+', ' ', text)
    text = text.lower()
    return text

def preprocess(text):
#     text = lemmatize(text)
    text = cleanText(text)
    return text