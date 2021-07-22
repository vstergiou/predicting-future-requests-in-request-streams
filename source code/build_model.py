import numpy as np
from numpy import array
np.random.seed(0) # for reproducibilitys
from numpy import array
from keras.models import Sequential, load_model
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers.core import  Activation, Dropout
import matplotlib.pyplot as pyplot
from tensorflow.keras.callbacks import Callback

def create_lstm(n_steps, n_features):

	model = Sequential()
	model.add(LSTM(50,input_shape=(n_steps, n_features),return_sequences=True))
	model.add(Dropout(0.2))
	model.add(LSTM(50,return_sequences=False))
	model.add(Dropout(0.2))
	model.add(Dense(1))
	model.add(Activation('tanh'))

	model.compile(loss="mse", optimizer="rmsprop")

	return model

def predict(x_input, scaler):

	# load model
	model = load_model('lstm_model.h5')

	# demonstrate prediction
	yhat = model.predict(x_input, verbose=0)
	yhat = np.reshape(yhat,(yhat.size,))
	inversed = scaler.inverse_transform(yhat)

	return inversed

