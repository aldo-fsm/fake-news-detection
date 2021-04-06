import numpy as np
from preprocessing import putEndDot, splitSentences
import pandas as pd
from sklearn.base import TransformerMixin

class SentenceRankingTransformer(TransformerMixin):
  def __init__(self, classifier, rankByProbaLabel):
    self.classifier = classifier
    self.rankByProbaLabel = rankByProbaLabel

  def fit(self, texts):
    return self

  def transform(self, texts):
    if (type(texts) is not pd.Series): texts = pd.Series(texts)
    sentenceLists = texts.apply(splitSentences)
    allSentences = [sent for sents in sentenceLists for sent in sents]
    numSentences = [len(item) for item in sentenceLists]
    probas = self.classifier.predict_proba(allSentences)
    textIndexes = np.repeat(range(len(sentenceLists)), numSentences)
    sentencesWithProbas = pd.DataFrame({
      'textIndex': textIndexes,
      'sentence': allSentences,
      **{ f'{label}Proba': proba for label, proba in zip(self.classifier.classes_, probas.T) },
    })
    sortedSentences = sentencesWithProbas.sort_values(
      by=['textIndex', f'{self.rankByProbaLabel}Proba'],
      ascending=[True, False]
    )
    return sortedSentences.groupby(by='textIndex').sentence.agg(lambda sentences: putEndDot('. '.join(sentences)))
