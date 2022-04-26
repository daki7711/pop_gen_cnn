import numpy as np
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv1D, MaxPooling1D, AveragePooling1D
from keras import backend as K
from random import shuffle, choice

batch_size = 256
epochs = 19
num_classes = 3

u = np.load("big_sim.npz")
xtrain, xtest, ytrain, ytest = [u[i] for i in ['xtrain', 'xtest', 'ytrain', 'ytest']]

ytest = keras.utils.to_categorical(ytest, num_classes)
ytrain = keras.utils.to_categorical(ytrain, num_classes)

model = Sequential()
model.add(Conv1D(256, kernel_size=2,
                 activation='relu',
                 input_shape=(xtest.shape[1], xtest.shape[2])))
model.add(Conv1D(128, kernel_size=2, activation='relu'))
model.add(AveragePooling1D(pool_size=2))
model.add(Dropout(0.25))
model.add(Conv1D(128, kernel_size=2, activation='relu'))
model.add(AveragePooling1D(pool_size=2))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='sigmoid'))
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adam(),
              metrics=['accuracy'])
print(model.summary())
model.fit(xtrain, ytrain, batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(xtest, ytest))
          
         
model.save(filepath='big.data.89.2.acc.mod')
