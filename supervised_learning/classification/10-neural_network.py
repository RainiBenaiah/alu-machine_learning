#!/usr/bin/env python3
"""Neural network Forward propagation"""


import numpy as np


class NeuralNetwork:
    '''
    neural network with one hidden layer
    '''
    def __init__(self, nx, nodes):
        """
        Class constructor
        """
        if not type(nx) is int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not type(nodes) is int:
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")
        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """
        Getter function for W1
        """
        return self.__W1

    @property
    def b1(self):
        """
        Getter function for b1
        """
        return self.__b1

    @property
    def A1(self):
        """
        Getter function for A1
        """
        return self.__A1

    @property
    def W2(self):
        """
        Getter function for W2
        """
        return self.__W2

    @property
    def b2(self):
        """
        Getter function for b2
        """
        return self.__b2

    @property
    def A2(self):
        """
        Getter function for A2
        """
        return self.__A2

    def forward_prop(self, X):
        """
        Calculates the forward propagation of the neural network
        """
        Z1 = np.matmul(self.__W1, X) + self.__b1
        self.__A1 = 1 / (1 + np.exp(-Z1))
        Z2 = np.matmul(self.__W2, self.__A1) + self.__b2
        self.__A2 = 1 / (1 + np.exp(-Z2))
        return self.__A1, self.__A2
