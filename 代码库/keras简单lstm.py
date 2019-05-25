from keras.models import Sequential
from keras.layers import LSTM
from keras.layers.core import Dense, Dropout
import keras.backend as K


def rmse(y_true, y_pred):
    return K.sqrt(K.mean(K.square(y_pred - y_true), axis=-1))

def build_model(input_shape=(1, 5), output_shape = 1):
    
    model = Sequential()
    model.add(LSTM(25, return_sequences=True, activation='relu', input_shape=input_shape))
    model.add(Dropout(0.3))
    model.add(LSTM(25, activation='relu'))
    model.add(Dropout(0.3))
    model.add(Dense(output_shape, activation='tanh'))
    model.compile(loss=rmse, optimizer='adam')
    return model

xtrain = xtrain.reshape((-1, 1, 5))
xtest = xtest.reshape((-1, 1, 5))

model = build_model()
model.summary()
hist = model.fit(xtrain,
                 ytrain,
                 epochs=100,
                 batch_size=1000,
                 verbose=1,
                 validation_data=(xtest, ytest))
