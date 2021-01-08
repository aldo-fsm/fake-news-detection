import plotly_express as px
import streamlit as st

from datasets import fake_br_corpus

train = fake_br_corpus.loadTrain()

train

st.write(
    px.pie(train, names='label'),
    px.pie(train, names='category'),
    px.histogram(train, x='category', color='label', barmode='group'),
)

# from preprocessing import preprocess
# from sklearn.feature_extraction.text import TfidfVectorizer

# tfidf = TfidfVectorizer(
#     preprocessor=preprocess,
#     ngram_range=(1,3),
#     max_features=1000
# )

# st.cache()
# def extractFeatures(texts):
#     return tfidf.fit_transform(texts)

# X = extractFeatures(train.text)

# from sklearn.decomposition import PCA

# pca = PCA(2)
# points = pca.fit_transform(X.toarray())
# # train[['pcax','y','z']] = points

# st.write(
#     px.scatter(x=points.T[0], y=points.T[1], color=train.label)
# )