import numpy as np
import activations as a

np.random.seed(0)

class Dense:
    def __init__(self, n_inputs: int, n_neurons: int, activation: str = None):
        self.n_inputs = n_inputs
        self.n_neurons = n_neurons
        
        self.weights = np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
        
        self.init_activation(activation)

    def init_activation(self, activation):
        if activation == 'sigmoid':
            self.activation = a.sigmoid
        elif activation == 'relu':
            self.activation = a.relu
        elif activation == 'softmax':
            self.activation = a.softmax
        else:
            self.activation = a.linear
        
    def activate(self, inputs):
        self.inputs = inputs
        self.outputs = self.activation(np.dot(inputs, self.weights) + self.biases)
        
        return self.outputs
    
    def derivate(self, inputs):
        return self.activation(inputs, derivative = True)