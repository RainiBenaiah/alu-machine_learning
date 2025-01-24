#!/usr/bin/env python3
'''Neural network'''


import numpy as np


class NeuralNetwork:
    '''
    neural network with one hidden layer
    '''

    def __init__(self, nx, nodes):
        '''
        Neuron class constructor
        '''
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        self.W1 = np.random.randn(nx, nodes)
        self.b1 = np.zeros((nodes, 1))
        self.A1 = 0
        self.W2 = np.random.randn(nodes, 1)
        self.b2 = 0
        self.A2 = 0
