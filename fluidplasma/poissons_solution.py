"""
Name  : poissons_solution.py
Author: Ajay Lotekar
e-mail: ablotekar@gmail.com
Date  : 2021-07-04 

DESC  :
"""
import numpy as np
from .kappa_density import kappa_density
from .periodic_boundary import periodic_boundary
from .filter3p import filter3p


def poissons_solution(x: float, z:float, k, dx, w, tol):
    """

    :param x: Electrostatic potential
    :param z: Ion density
    :param k: kappa index
    :param dx: Grid size -space
    :param w:  SOR method coefficient
    :param tol:  Tolerance for accuracy
    :return:  Electrostatic potential
    """

    pp = 2.0

    while pp > tol:
        xold = np.array(x, dtype='float32')
        for i in range(2, max(x.shape) - 3):
            po = 0.5 * (x[i + 1] + x[i - 1]
                        + (z[i] - kappa_density(x[i], k)) * dx * dx)
            x[i] = po + w * (po - xold[i])

        x = periodic_boundary(x)
        diff = xold - x
        diff = np.abs(diff)
        pp = np.max(diff)

    x = filter3p(x)
    #print("%10.3E" % (pp))
    return x
