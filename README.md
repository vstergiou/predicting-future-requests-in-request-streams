# predicting-future-requests-in-request-streams

# Overview 

Being able to predict future requestsin a requeststream is vital in building
effective caches and designing betterreplacement policies and prefetching
techniques.

In this project, an LSTM neural network architecture is proposed that predicts the next request
given a sequence of previous requests. The development environment
used is Tensorflow with Keras.

## Train and predict commands 

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
