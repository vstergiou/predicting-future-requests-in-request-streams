import numpy as np
from numpy import array
np.random.seed(0) # for reproducibility
import pandas as pd
from pandas import Series
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def split_sequence(sequence, n_steps):
	X, y = list(), list()
	for i in range(len(sequence)):
		# find the end of this pattern
		end_ix = i + n_steps
		# check if we are beyond the sequence
		if end_ix > len(sequence)-1:
			break
		# gather input and output parts of the pattern
		seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
		X.append(seq_x)
		y.append(seq_y)
	return array(X), array(y)

def normalize_data(data):

	series = Series(data)
	# prepare data for normalization
	values = series.values
	values = values.reshape((len(values), 1))
	# train the normalization
	scaler = StandardScaler()
	scaler = scaler.fit(values)

	# normalize the dataset and print
	standardized = scaler.transform(values)

	return standardized,scaler 

def load_data(filename,n_steps, n_features):

	data = pd.read_excel(filename,header=None)
	lines = []
	lines = data[0].tolist()
	raw_seq = [int(line,16) for line in lines]

	raw_seq_norm , sth= normalize_data(raw_seq)

	# split into train and test sets

	train_size = int(len(raw_seq_norm) * 0.75)
	test_size = len(raw_seq_norm) - train_size
	train, test = raw_seq_norm[0:train_size], raw_seq_norm[train_size:len(raw_seq_norm)]

	# split normalized-input  into samples

	X, Y = split_sequence(train, n_steps)
	x_train, x_val , y_train, y_val = train_test_split(X,Y,test_size=0.1)
	x_test, y_test = split_sequence(test, n_steps)

	# reshape from [samples, timesteps] into [samples, timesteps, features]

	x_train = x_train.reshape((x_train.shape[0], x_train.shape[1], n_features))

	x_test = x_test.reshape((x_test.shape[0], x_test.shape[1], n_features))

	return x_train, y_train, x_val, y_val, x_test, y_test,sth

def load_predict_file(filename):

	#define input used for prediction
	data = pd.read_excel(filename,header=None)
	
	lines = []
	lines = data[0].tolist()
	raw_seq = [int(line,16) for line in lines]
	x_input =array(raw_seq)
	return x_input