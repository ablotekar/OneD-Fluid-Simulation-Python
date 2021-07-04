"""
Name  : gaussian.py
Author: Ajay Lotekar
e-mail: ablotekar@gmail.com
Date  : 2021-07-04 

DESC  :
"""
import numpy as np
import fluidplasma as fp


def gaussian(x: float, a, l0, c):
    r"""Gaussian function

    It return the Gaussian function output for given array.

    Parameters
    ----------
    x : xarray.Dataset
      Array at which Gaussian calculate
    a : flot
      Amplitude of the Gaussian peak
    l0: float
      Width of the amplitude
    c : float
      Position of the Gaussian peak

    Example
    -------
    >> x = np.linspace(1,1000, 1000)
    >> n = gaussian(x, 2, 10, 50)

    :type x: float
    """

    y = np.zeros(x.shape)
    for i in range(0, max(x.shape) - 1):
        p = ((x[i] - c) / l0) ** 2
        y[i] = a * np.exp(-1 * p)

    y = fp.periodic_boundary(y)
    return y
