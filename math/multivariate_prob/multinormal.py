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
        """
        pdf function that returns the pdf of the data point
        """
        if not isinstance(x, np.ndarray) or len(x.shape) != 2:
            raise TypeError("x must be a numpy.ndarray")
        if (x.shape[0] != self.mean.shape[0] or
                x.shape[1] != 1):
            raise ValueError(f"x must have the shape ({self.mean.shape[0]}, 1)")

        n = self.mean.shape[0]
        det = np.linalg.det(self.cov)
        inv = np.linalg.inv(self.cov)
        x_minus_mean = x - self.mean

        pdf_value = (1 / ((2 * np.pi) ** (n / 2) * np.sqrt(det)) *
                     np.exp(-0.5 * np.dot(np.dot(x_minus_mean.T, inv),
                                           x_minus_mean)))

        return pdf_value.item()
