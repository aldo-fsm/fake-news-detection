import re
import spacy

class TextPreprocessor:
    def __init__(self, clean=True, lemmatize=False):
        if lemmatize:
            self.nlp = spacy.load('pt')
        self.shoudClean = clean
        self.shoudLemmatize = lemmatize

    def lemmatize(self, text):
        tokens = self.nlp(text)
        lemmas = [token.lemma_ for token in tokens]
        return ' '.join(lemmas)

    def cleanText(self, text):
        text = re.sub(r'[0-9"\(\)\,\:]+', ' ', text)
        text = re.sub(r'[\n ]+', ' ', text)
        text = text.lower()
        return text

    def preprocess(self, text):
        if self.shoudLemmatize:
            text = self.lemmatize(text)
        if self.shoudClean:
            text = self.cleanText(text)
        return text
