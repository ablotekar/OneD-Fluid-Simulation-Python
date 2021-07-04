"""
Name  : kappa_density.py
Author: Ajay Lotekar
e-mail: ablotekar@gmail.com
Date  : 2021-07-04 

DESC  :
"""


def kappa_density(x, k):
    """ Kappa density function

    :param x: phi in kappa density function (it must be scalar)
    :param k: kappa index
    :return: kappa density value
    """
    p = -k + 0.5  # Power of kappa function
    b = 1.0 / (k - 1.5)  # Denominator in kappa function
    y = (1 - b * x) ** p
    return y
