#!/usr/bin/env python3
"""Placeholders"""
import tensorflow as tf


def create_placeholders(nx, classes):
    """
    Create placeholders
    """

    x = tf.placeholder("float", [None, nx], name="x")
    y = tf.placeholder("float", [None, classes], name="y")

    return x, y
