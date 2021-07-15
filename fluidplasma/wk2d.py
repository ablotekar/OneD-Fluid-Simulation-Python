"""
Name  : wk2d.py
Author: Ajay Lotekar
e-mail: ablotekar@gmail.com
Date  : 2021-07-15 

DESC  :
"""
import numpy as np
import math as mt


def wk2d(z, dx, dt):
    """

    :param z: Matrix which 2D fft need to calculate row = time, column = space
    :param dx: Spatial grid size
    :param dt: Temporal grid size
    :return: z 2D fft , k wave number array and w frequency array
    """

    mm = z.shape[0]  # Size of matrix in y direction (time)
    nx = z.shape[1]  # Size of the matrix in x direction (space)
    nx1 = nx - 1
    kmin = 2 * (mt.pi) / (nx1 * dx)  # Minimum wavelength can resolve
    wmin = 2 * (mt.pi) / (nx1 * dt)  # Mininum frequency can resolve

    # Wave number array
    k = np.arange(start=-nx1 / 2, stop=nx1 / 2, step=1) * kmin
    # Frequency array
    w = np.arange(start=-mm / 2, stop=mm / 2, step=1) * wmin
    w = np.delete(w, int(np.fix(mm / 2)))  # Removing zero
    z = np.fft.fft2(z)  # 2D fft
    z = np.fft.fftshift(z)
    z = 2 * np.square(np.abs(z)) / (nx * mm)
    z = 10 * np.log10(z)

    return z, k, w

