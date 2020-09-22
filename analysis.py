import pandas as pd
import glob

def negative(x):
	if x is not None and x != 0:
		return x * -1
	else:
		return None

def change(frame):
	frame = frame.diff(axis=1)
	for column in frame.columns:
		frame[column] = frame[column].apply(negative)

	frame = frame.sort_values(frame.columns[len(frame.columns) - 1], ascending = False)
	return frame	

all_files = glob.glob("./logs/*.csv")
pd.options.display.float_format = '{:.1f}'.format

li = []

for filename in all_files:

    df = pd.read_csv(filename, index_col=0, header=0)

    li.append(df)

try:
	frame = pd.concat(li, axis=1, join='outer', ignore_index=False, sort=False)	
	frame = frame.reindex(sorted(frame.columns), axis=1)
	print('CHANGES OVER TIME')
	print(change(frame))
	frame['Rank'] = frame.mean(axis=1)
	print('\nOVERALL RANK')
	print(frame.sort_values('Rank'))
except ValueError:
	print("No Files Found! Get Data using retrieveSource.py")
