import plotly_express as px
import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
from datasets import fake_br_corpus

train = fake_br_corpus.loadTrain()#.sample(100)

train

st.write(
    px.pie(train, names='label'),
    px.pie(train, names='category'),
    px.histogram(train, x='category', color='label', barmode='group'),
)

from preprocessing import preprocess
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(
    preprocessor=preprocess,
    ngram_range=(1,3),
    max_features=1000
)

def countFeatures(X):
    return pd.DataFrame(
        [(label, (row>0).sum()) for label, row in zip(train.label, X)], columns=['label', 'numFeatures']
    )

st.cache()
def extractFeatures(texts):
    # texts = train.text
    return tfidf.fit_transform(texts).toarray()

X = extractFeatures(train.text)

featureCounts = countFeatures(X)

st.write(
    X,
    featureCounts,
    featureCounts.sort_values('numFeatures'),
    px.violin(featureCounts, y='numFeatures', color='label'),
    px.histogram(featureCounts, x='numFeatures', color='label', barmode='stack'),
)

shouldCutFeatures = st.checkbox('Cut Features')
numFeatures = 50
# numFeatures = featureCounts['numFeatures'].min()
st.write(f'Cutting to {50}')

def aaa(a, cut):
    orderFactor = np.arange(len(a))*1E-20
    a = a + orderFactor
    return np.where(a >= np.sort(a)[-cut], a - orderFactor, 0)

X = np.array(
    [aaa(a, numFeatures) for a in X]
)

featureCounts = countFeatures(X)

st.write(
    X,
    featureCounts,
    featureCounts.sort_values('numFeatures'),
    px.violin(featureCounts, y='numFeatures', color='label'),
)

# from sklearn.decomposition import PCA
# reducer = PCA(2)

from sklearn.decomposition import TruncatedSVD
reducer = TruncatedSVD(2)

# from sklearn.decomposition import LatentDirichletAllocation
# lda = LatentDirichletAllocation(50)
# X = lda.fit_transform(X)

points = reducer.fit_transform(X)
points = pd.DataFrame(points, columns=['x', 'y'])
points['label'] = featureCounts.label
points['numFeatures'] = featureCounts.numFeatures
points['numWords'] = train.text.apply(lambda text: len(text.split(' '))).values
# train[['pcax','y','z']] = points
st.write(
    px.scatter(points, x='x', y='y', color='label', size='numFeatures'),
    px.scatter(points, x='x', y='y', color='label', size='numWords'),
)
