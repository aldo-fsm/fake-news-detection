import os
import pandas as pd

DATASET_PATH = 'datasets/fake_br_corpus'

def loadTrain():
    train = pd.read_csv(os.path.join(DATASET_PATH, 'train.csv'))
    return train

def loadTest():
    test = pd.read_csv(os.path.join(DATASET_PATH, 'test.csv'))
    return test
