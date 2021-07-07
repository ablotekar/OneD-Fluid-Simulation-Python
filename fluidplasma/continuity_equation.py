"""
Name  : continuity_equation.py
Author: Ajay Lotekar
e-mail: ablotekar@gmail.com
Date  : 2021-07-04 

DESC  :
"""
from .fd4 import fd4
from .periodic_boundary import periodic_boundary
from .filter3p import filter3p


def continuity_equation(x, y, z, ic, dx, dt):
    """ Continuty equation

    :param x: Ion velocity
    :param y: Ion density
    :param z: Electrostatic potential
    :param ic: Time index 1 or 0
    :param dx: Grid size - space
    :param dt: Grid size - time
    :return: upgraded value of ion density and velocity at next
            time step
    """
    jc = 1 - ic # Previous time index
    fd0 = fd4(x[:, jc], dx)
    fd1 = fd4(y[:, jc], dx)
    fd2 = fd4(z[:, jc], dx)

    for i in range(2, max(x.shape) - 3):
        y[i, ic] = y[i, ic] - dt * (y[i, jc] * fd0[i] - x[i, jc] * fd1[i])
        x[i, ic] = x[i, ic] - dt * (x[i, jc] * fd0[i] + fd2[i])

    # Updating boundary's
    x[:, ic] = periodic_boundary(x[:, ic])
    y[:, ic] = periodic_boundary(y[:, ic])

    # Filtering numerical noise
    x[:, ic] = filter3p(x[:, ic])
    y[:, ic] = filter3p(y[:, ic])

    return x, y
