n Neural network"""


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

        self..__W1 = np.random.randn(nx, nodes)
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.randn(nodes, 1)
        self.__b2 = 0
        self.__A2  = 0

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

    def forward_prop(self, X):
        """
        Forward propagation function
        """
        self.__A1 = 1 / (1 + np.exp(-(np.dot(self.__W1.T, X) + self.__b1)))
        self.__A2 = 1 / (1 + np.exp(-(np.dot(self.__W2.T, self.__A1) + self.__b2)))
        return self.__A1, self.__A2

    def cost(self, Y, A):
        """
        Cost of the model
        """
        m = Y.shape[1]
        return -np.sum((Y * np.log(A)) + ((1 - Y) * np.log(1.0000001 - A))) / m

    def evaluate(self, X, Y):
        """
        Evaluates the neural network
        """

        self.forward_prop(X)
        return np.round(self.__A2).astype(int), self.cost(Y, self.__A2)

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """
        Calculates one pass of gradient descent on the neural network
        """
        m = Y.shape[1]
        dz2 = A2 - Y
        dw2 = np.matmul(A1, dz2.T) / m
        db2 = np.sum(dz2, axis=1, keepdims=True) / m
        dz1 = np.matmul(self.__W2, dz2) * (A1 * (1 - A1))
        dw1 = np.matmul(X, dz1.T) / m
        db1 = np.sum(dz1, axis=1, keepdims=True) / m
        self.__W2 = self.__W2 - (alpha * dw2).T
        self.__b2 = self.__b2 - alpha * db2
        self.__W1 = self.__W1 - (alpha * dw1).T
        self.__b1 = self.__b1 - alpha * db1

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """
        Trains the neural network
        """
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations < 1:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, (int, float)):
            raise TypeError("alpha must be a number")
        if alpha < 0:
            raise ValueError("alpha must be positive")
        for i in range(iterations):
            self.forward_prop(X)
            self.gradient_descent(X, Y, self.__A1, self.__A2, alpha)
        return self.evaluate(X, Y)
