import pandas as pd
import glob

all_files = glob.glob("./logs/*.csv")

li = []

for filename in all_files:

    df = pd.read_csv(filename, index_col=0, header=0)

    li.append(df)

try:
	frame = pd.concat(li, axis=1, join='outer', ignore_index=False, sort=False)
	frame['Rank'] = frame.mean(axis=1)
	frame = frame.reindex(sorted(frame.columns), axis=1)
	print(frame.sort_values('Rank'))
except ValueError:
	print("No Files Found! Get Data using retrieveSource.py")
