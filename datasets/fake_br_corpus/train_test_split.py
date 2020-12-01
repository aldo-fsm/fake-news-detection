import pandas as pd
from sklearn.model_selection import train_test_split
from . import DATASET_PATH
import os

if __name__ == '__main__':
    dataset = pd.read_csv(os.path.join(DATASET_PATH, 'full_texts.csv'))
    train, test = train_test_split(dataset, test_size=0.15)
    train.to_csv(os.path.join(DATASET_PATH, 'train.csv'), index=False)
    test.to_csv(os.path.join(DATASET_PATH, 'test.csv'), index=False)