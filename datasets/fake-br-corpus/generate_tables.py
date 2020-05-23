import os
import pandas as pd
from constants import METADATA_KEYS

def dirToDataframe(dataDir):
    labels = [dirName for dirName in os.listdir(dataDir) if 'meta-information' not in dirName]
    data = []
    for label in labels:
        labelDir = os.path.join(dataDir, label)
        metaDir = os.path.join(dataDir, f'{label}-meta-information')
        for filename in os.listdir(labelDir):
            index = int(filename.replace('.txt', ''))
            meta_filename = f'{index}-meta.txt'
            row = {}
            with open(os.path.join(labelDir, filename)) as f:
                row.update({
                    'text': f.read(),
                    'label': label,
                    'filename': filename
                })
            with open(os.path.join(metaDir, meta_filename)) as f:
                lines = [line.strip() for line in f.readlines()]
                row.update({
                    key: value for key, value in zip(METADATA_KEYS, lines)
                })
            data.append(row)
    return pd.DataFrame(data)

if __name__ == '__main__':
    fullTexts = dirToDataframe('full_texts')
    fullTexts.to_csv('full_texts.csv', index=False)

    # sizeNormalizedTexts = dirToDataframe('size_normalized_texts')
    # sizeNormalizedTexts.to_csv('size_normalized_texts.csv', index=False)