import numpy as np
import keras
from keras import layers

input_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
output_data = np.array([[0], [1], [1], [0]])


model = keras.Sequential()
model.add(layers.Dense(2, input_dim=2, activation='relu')) # 2 neurons in input layer
#model.add(layers.Dense(2, activation='tanh'))
model.add(layers.Dense(1, activation='sigmoid'))

model.summary()