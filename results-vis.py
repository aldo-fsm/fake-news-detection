import streamlit as st
import plotly_express as px
from experiments.classical_ml import loadResults

results = loadResults().sort_values('mean_test_score', ascending=False)
# results = loadResults().sort_values('rank_test_score')
results['clf_name'] = results.param_clf.apply(lambda clf: clf.split('(')[0])

st.write(
    results,
    results[['params', 'mean_test_score', 'rank_test_score']],
)

st.write(
    px.bar(results, y='mean_test_score', x=results.index),
    px.box(results, y='mean_test_score', color='clf_name'),
)


clfs = st.multiselect('Clf', results.clf_name.unique())
if (len(clfs)):
    st.write(
        px.box(
            results[results.clf_name.isin(clfs)],
            y='mean_test_score', color='param_vect__ngram_range'
        ),
        px.box(
            results[results.clf_name.isin(clfs)],
            y='mean_test_score', color='param_vect__max_features'
        ),
    )