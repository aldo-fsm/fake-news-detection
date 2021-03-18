import numpy as np
from sklearn.base import TransformerMixin
from scipy.special import softmax

class SoftmaxTransformer(TransformerMixin):
    def fit(self, X):
        return self

    def transform(X):
        return np.apply_along_axis(softmax, 1, X)