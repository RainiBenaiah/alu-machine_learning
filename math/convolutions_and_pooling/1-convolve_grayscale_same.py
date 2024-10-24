#!/usr/bin/env python3
'''
defines a same convolution padding function
'''
import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """
    Function to perform a same convolution on grayscale images
    Returns:numpy.ndarray - shape (m, h, w)
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    ph, pw = padding

    output = np.zeros((m, h, w))

    padded_images = np.pad(
        images,
        ((0, 0), (ph, ph), (pw, pw))
        )

    for i in range(h):
        for j in range(w):
            output[:, i, j] = np.sum(
                padded_images[:, i:i+kh, j:j+kw] * kernel,
                axis=(1, 2)
                )

    return output
