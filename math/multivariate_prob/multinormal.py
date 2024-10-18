#!/usr/bin/env python3
'''
Class for multinormal distribution
'''
import numpy as np


class MultiNormal:
    """
    MultiNormal class that represents a multinormal distribution.
    """
    def __init__(self, data):
        """
        Constructor
        """
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        if data.shape[1] < 2:
            raise ValueError(
                "data must contain multiple data points"
            )
        self.mean = np.mean(data, axis=1).reshape(-1, 1)
        centered_data = data - self.mean
        self.cov = np.dot(centered_data, centered_data.T) / (data.shape[1] - 1)

     def pdf(self, x):
        '''
        Constructor
        '''
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        d = self.cov.shape[0]
        if x.shape != (d, 1):
            raise ValueError("x must have the shape ({}, 1)".format(d))

        det = np.linalg.det(self.cov)
        inv = np.linalg.inv(self.cov)
        centered_x = x - self.mean
        expo = -0.5 * np.dot(np.dot(centered_x.T, inv), centered_x)
        pdf_nom = 1 / ((2 * np.pi) ** (d / 2) * np.sqrt(det))
        pdf_value = pdf_nom * np.exp(expo)

        return float(pdf_value)   


