import numpy as np
from framework.datasets import rgb
from framework.models import Sequential
from framework.layers import Dense
from framework.activations import ReLU, Sigmoid
from framework.optimizers import SGD
from framework.initializers import GlorotNormal, HeUniform
from framework.regularizers import L1, L2

def get_data():
    return rgb.get_normalized()

def get_color():
    user_input = input('\nInput:  ')
    
    if ',' in user_input:
        color = np.asarray([int(x) for x in user_input.split(',')])
    else:
        color = np.asarray([int(user_input.lstrip('#')[x:x + 2], 16) for x in (0, 2, 4)])
    
    return color / 255

def main():
    inputs, targets = get_data()
    
    # 3-3-3-1 (classifier)
    model = Sequential([
        Dense(3, activation = ReLU(), initializer = HeUniform(), regularizers = [L1(amount = 1e-4)]),
        Dense(3, activation = ReLU(), initializer = HeUniform(), regularizers = [L1(amount = 1e-4)]),
        Dense(1, activation = Sigmoid(), initializer = HeUniform(), regularizers = [L1(amount = 1e-4)])
    ])
    
    model.compile(optimizer = SGD(learning_rate = 0.01, momentum = 0.9))
    
    model.fit(inputs, targets, batch_size = 8, n_epochs = 100)
    
    # Prediction
    prediction = int(np.squeeze(model.predict(get_color())))
    
    print('Output: {} ({})\n'.format(prediction, 'black' if prediction == 0 else 'white'))
    
if __name__ == "__main__":
    #if wmi.WMI().Win32_VideoController()[0].AdapterCompatibility.lower() == 'nvidia':
    #    import cupy as np
    #else:
    #    import numpy as np

    main()