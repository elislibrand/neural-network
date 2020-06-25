import numpy as np
from models import Sequential
from layers import Dense

inputs = [[1, 2, 3],
          [2, 3, 4],
          [3, 4, 5],
          [4, 5, 6],
          [5, 6, 7]]

model = Sequential()

model.add(Dense(n_inputs = 3, n_neurons = 3, activation = 'relu'))
model.add(Dense(n_inputs = 3, n_neurons = 1, activation = 'sigmoid'))