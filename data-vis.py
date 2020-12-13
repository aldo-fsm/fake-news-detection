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
