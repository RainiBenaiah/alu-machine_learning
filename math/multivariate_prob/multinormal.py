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
            raise ValueError("data must contain multiple data points")
        self.mean = np.mean(data, axis=1).reshape(-1, 1)
        centered_data = data - self.mean
        self.cov = np.dot(centered_data, centered_data.T) / (data.shape[1] - 1)

    def pdf(self, x):
        """
        Method that calculates the PDF at a data point
        """
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        if len(x.shape) != 2 or x.shape[1] != 1:
            raise ValueError(
                "x must have the shape ({}, 1)".format(self.mean.shape[0])
            )
        n = self.mean.shape[0]
        x_m = x - self.mean
        pdf = (
                1 / np.sqrt((2 * np.pi) ** n * np.linalg.det(self.cov))
                * np.exp(
                    -np.dot(np.dot(x_m.T, np.linalg.inv(self.cov)), x_m) / 2)
        )
        return pdf.flatten()[0]
