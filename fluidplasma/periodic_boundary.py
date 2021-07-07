"""
Name  : periodic_boundary.py
Author: Ajay Lotekar
e-mail: ablotekar@gmail.com
Date  : 2021-07-04 

DESC  :
"""


def periodic_boundary(z):
    """ Periodic boundary

    Function return the input array after updating boundary

    :param z:
    """
    z[0] = z[-4]
    z[1] = z[-3]
    z[-2] = z[2]
    z[-1] = z[3]
    return z
