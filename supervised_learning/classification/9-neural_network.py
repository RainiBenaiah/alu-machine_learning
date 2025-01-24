#!/usr/bin/env python3
"""Private neural network"""


import numpy as np


class NeuralNetwork:
    '''
    neural network with one hidden layer
    '''
    def __init__(self, nx, nodes):
        '''
        Neuron class constructor
        '''
        if not type(nx) is int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not type(nodes) is int:
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        self.W1 = np.random.randn(nodes, nx)
        self.b1 = np.zeros((nodes, 1))
        self.A1 = 0
        self.W2 = np.random.randn(1, nodes)
        self.b2 = 0
        self.A2 = 0

    @property
    def W1(self):
        '''
        getter function
        '''
        return self.__W1

    @property
    def b1(self):
        '''
        getter function
        '''
        return self.__b1

    @property
    def A1(self):
        '''
        getter function
        '''
        return self.__A1

    @property
    def W2(self):
        '''
        getter function
        '''
        return self.__W2

    @property
    def b2(self):
        '''
        getter function
        '''
        return self.__b2

    @property
    def A2(self):
        '''
        getter function
        '''
        return self.__A2
