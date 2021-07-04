"""
Name  : fd4.py
Author: Ajay Lotekar
e-mail: ablotekar@gmail.com
Date  : 2021-07-04 

DESC  :
"""
import numpy as np


def fd4(z, xd):
    """ Forth order central finite difference

    Function compute first order derivative of given array by using 4th
    order central finite difference scheam

    :param z: Input array
    :param xd: Grid size
    :return: y: output vector
    """
    y = np.zeros(z.shape)
    for i in range(2, max(z.shape) - 3):
        y[i] = (8 * z[i + 1] - 8 * z[i - 1] - z[i + 2] + z[i - 2]) / (12 * xd)
    return y
