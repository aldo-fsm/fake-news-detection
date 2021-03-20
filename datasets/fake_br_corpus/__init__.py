import os
import pandas as pd

DATASET_PATH = 'datasets/fake_br_corpus'

def loadTrain(balanced=False):
    datasetFilename = 'train_balanced.csv' if balanced else 'train.csv'
    train = pd.read_csv(os.path.join(DATASET_PATH, datasetFilename))
    return train

def loadTest():
    test = pd.read_csv(os.path.join(DATASET_PATH, 'test.csv'))
    return test
