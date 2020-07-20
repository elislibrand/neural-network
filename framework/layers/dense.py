import numpy as np
from framework import activations
from framework.initializers import Glorot

np.random.seed(0)

class Dense:
    def __init__(self, n_neurons, activation = None, initializer = Glorot(), regularizers = []):
        self.n_neurons = n_neurons
        
        self.activation = activations.get(activation)
        
        self.initializer = initializer
        self.regularizers = regularizers
    
    def build(self, n_inputs, seed):
        self.n_inputs = n_inputs
        
        #np.random.seed(seed)
        
        self.weights = self.initializer.initialize(self.n_inputs, self.n_neurons)
        self.biases = np.zeros((1, self.n_neurons))

        self.previous_adjustment_weights = np.zeros(self.weights.shape)
        self.previous_adjustment_biases = np.zeros(self.biases.shape)
        
    def activate(self, inputs):
        self.inputs = inputs
        
        self.outputs = self.activation(self.inputs @ self.weights + self.biases)
        
        return self.outputs
    
    def differentiate(self, inputs):
        return self.activation(inputs, derivative = True)
    
    def regularize_gradients(self):
        for regularizer in self.regularizers:
            regularizer.regularize_gradients(self)
            
    def regularize_weights(self):
        for regularizer in self.regularizers:
            regularizer.regularize_weights(self)