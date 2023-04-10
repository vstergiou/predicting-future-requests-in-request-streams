# LSTM Neural Network for Request Prediction

This project aims to build an LSTM neural network architecture that predicts the next request given a sequence of previous requests. This is useful in building effective caches and designing better replacement policies and prefetching techniques.

The development environment used for this project is Tensorflow with Keras. The network consists of two LSTM layers with 50 neurons each, followed by dropout layers with rate 0.2, a dense layer, and a layer that applies the activation function tanh. The training data is normalized to reflect percentage changes from the start of each window, and predictions are denormalized after training.

## Files in the Repository
train_predict.py: Python script for training and predicting using the LSTM network
predictedMemReference.xlsx: Excel file containing the predictions given by the network
README.md: This file

## How to Use
# Dependencies
* Python 3.7 or later
* Tensorflow
* Keras
* Pandas
# Train the Network
To train the network, run the following command in the terminal:
`python train_predict.py train ./[file with train data].xlsx
`

Replace [file with train data] with the name of the Excel file containing the training data.

# Make Predictions
To make predictions using the trained network, run the following command in the terminal:

`python train_predict.py predict ./[file with data for prediction].xlsx
`

Replace [file with data for prediction] with the name of the Excel file containing the data for prediction.

# Note
* Training took approximately 45 minutes for 50 epochs.
* Each prediction (on every 999 samples) took 3.25 seconds on average to complete.

## References
1. https://en.wikipedia.org/wiki/Long_short-term_memory
2. http://colah.github.io/posts/2015-08-Understanding-LSTMs/
3. https://machinelearningmastery.com/how-to-scale-data-for-long-short-term-memory-networks-in-python/
--------
Compile command for training: 
```
python train_predict.py train ./[file with
train data].xlsx

```

Compile command for prediction: 
```
python train_predict.py predict./[file
with data for prediction].xlsx
```
