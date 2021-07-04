"""
Name  : filter3p.py
Author: Ajay Lotekar
e-mail: ablotekar@gmail.com
Date  : 2021-07-04 

DESC  :
"""
from .periodic_boundary import periodic_boundary


def filter3p(z):
    """

    :param z:
    :return:
    """
    for i in range(3, max(z.shape) - 3):
        z[i] = (-1 * z[i - 2] + 4 * z[i - 1] + 10 * z[i]
                + 4 * z[i + 1] - z[i + 2]) / 16
    z = periodic_boundary(z)
    return z