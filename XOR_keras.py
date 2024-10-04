import numpy as np
import tensorflow as tf
import keras
from keras import layers
import matplotlib.pyplot as plt

input_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
output_data = np.array([[0], [1], [1], [0]])


model = keras.Sequential()
model.add(layers.Dense(2, input_dim=2, activation='relu')) # 2 neurons in input layer
model.add(layers.Dense(5, activation='tanh'))
model.add(layers.Dense(1, activation='sigmoid'))

model.summary()

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(input_data, output_data, epochs=1000)

plt.plot(history.history['accuracy'])
plt.show()
plt.plot(history.history['loss'])
plt.show()

_, accuracy = model.evaluate(input_data, output_data)
print(f"Accuracy: {accuracy * 100:.2f}%")

predictions = model.predict(input_data)
predictions = np.round(predictions).astype(int)

print("Predictions:")
for i in range(len(input_data)):
    print(f"Input: {input_data[i]} => Predicted Output: {predictions[i]}, Actual Output: {output_data[i]}")
