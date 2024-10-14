#!/usr/bin/env python3
'''
class for multinormal distribution
'''
import numpy as np


class MultiNormal:
      """
      Multinormal class that represents a multinormal dist
      """
      def __init__(self, data):
          """
          Constructor
          """
          if not isinstance(data, np.ndarray) or len(data.shape) != 2:
              raise TypeError("data must be a 2D numpy.ndarray")
          if data.shape[0] < 2:
              raise ValueError("data must contain multiple data points")
          self.mean = np.mean(data, axis=1).reshape(-1, 1)
          self.cov = np.dot(data - self.mean, data.T) / (data.shape[1] - 1)
