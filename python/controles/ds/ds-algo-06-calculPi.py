# -*- coding: utf-8 -*-
 
from math import *

#-----------------------------------------------------------------------
def calculPi(n):
    """
    y = calculPi(n)
    calcul de pi à l'ordre n
    
    >>> from math import fabs, pi
    >>> fabs(pi - calculPi(1)) < 1.
    True
    >>> fabs(pi - calculPi(1000000)) < 1.e-6
    True
    """
    assert type(n) is int and n >= 0

    y = 0
    for k in range(1,n+1):
        u = 1./(k*k)
        y = y + u
    return sqrt(6*y)

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
