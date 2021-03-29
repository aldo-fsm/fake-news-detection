import pandas as pd
import os
import glob

RESULTS_PATH = 'experiments/classical_ml/results'

def loadResults() -> pd.DataFrame:
    results = pd.DataFrame()
    for path in glob.glob(os.path.join(RESULTS_PATH, '*.csv')):
        results = results.append(
            pd.read_csv(path),
            ignore_index=True,
        )
    return results