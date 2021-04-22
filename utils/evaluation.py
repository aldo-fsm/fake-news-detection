import pandas as pd
import seaborn as sns
from sklearn.metrics import classification_report, accuracy_score

def evaluate(clf, X_test, ytrue):
    ypred = clf.predict(X_test)
    print(classification_report(ytrue, ypred))
    print('accuracy:', accuracy_score(ytrue, ypred))
    return ypred


def sizeDistributionByLabel(labels, sizes, **kwargs):
    df = pd.DataFrame(dict(
        label=labels,
        size=sizes,
    ))
    return sns.histplot(df, x='size', hue='label', multiple='fill', **kwargs)
