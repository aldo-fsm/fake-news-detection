import re
import nltk
nltk.download('stopwords')
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

def splitSentences(text, abbreviations=[]):
    # !!! vira .
    text = re.sub('!+', '.', text)
    # ... vira .
    text = re.sub(r'\.+', '.',text)

    # pontos dentro de parenteses são removidos
    cleanChunk = lambda match : match.string[match.start():match.end()].replace('.', '')
    for start, end in [['\(', '\)'], ['\"', '\"'], ["\'", "\'"]]:
        chunkRegex = fr'(?<=[{start}])[^{start}{end}]*(?=[{end}])'
        text = re.sub(chunkRegex, cleanChunk, text)

    for abbreviationsEntity in abbreviations:
        for abbreviation in abbreviationsEntity[ENTITY.SYNONYM_LIST_FIELD]:
            text = re.sub(rf' ["\(\']?{abbreviation}\.', f' {abbreviation}',text)

    # não tem numero antes ?<![0-9])\. ou
    # não tem numero depois \.(?![0-9])
    sentences = re.split(r'(?<![0-9])\.|\.(?![0-9])', text)
    return [sentence for sentence in sentences if sentence]

def putEndDot(text: str) -> str:
    text = text.strip()
    lastChar = text[-1]
    if lastChar in ['.', '!', '?']:
        text = text[:-1]
    text = text + '.'
    return text
