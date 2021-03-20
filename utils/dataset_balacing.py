import pandas as pd

def numWordBalancing(dataset: pd.DataFrame, progress=lambda it: it) -> pd.DataFrame :
    dataset = dataset.copy()
    dataset['words'] = dataset.text.apply(lambda text: text.split(' '))
    dataset['numWords'] = dataset.words.apply(lambda words: len(words))
    
    fakes = dataset[dataset.label == 'fake']
    trues = dataset[dataset.label == 'true']

    balanced = pd.DataFrame()

    for i, fakeRow in progress(fakes.sort_values(by='numWords').iterrows(), total=len(fakes)):
        smallestTrue, trues = popSmallest(trues)
        truncatedTrue = truncateToSize(smallestTrue, fakeRow.numWords)
        balanced = balanced.append(fakeRow, ignore_index=True)
        balanced = balanced.append(truncatedTrue, ignore_index=True)
        if (len(trues) == 0): break;

    return balanced

def truncateToSize(row: pd.Series, targetSize) -> pd.Series:
    row = row.copy()
    row['originalText'] = row.text
    row['words'] = row.words[:targetSize]
    row['numWords'] = len(row.words)
    row['text'] = ' '.join(row.words)
    return row

def popSmallest(dataset: pd.DataFrame) -> tuple([pd.Series, pd.DataFrame]):
    dataset = dataset.copy()
    minimumSize = dataset.numWords.min()
    smallests = dataset[dataset.numWords == minimumSize]
    remaining = dataset[dataset.numWords != minimumSize]
    remaining = pd.concat([smallests.iloc[1:], remaining])
    smallest = smallests.iloc[0]
    return smallest, remaining