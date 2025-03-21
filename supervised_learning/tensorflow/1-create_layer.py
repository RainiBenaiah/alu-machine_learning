#!/usr/bin/env python3
"""layers"""

import tensorflow as tf


def create_layer(prev, n, activation):
    """
    Create a layer
    """

    initializer = tf.contrib.layers.variance_scaling_initializer(
        mode="FAN_AVG")
    layer = tf.layers.Dense(units=n,
                            activation=activation,
                            kernel_initializer=initializer,
                            name='layer')

    return layer(prev)
