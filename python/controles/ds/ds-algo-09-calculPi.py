# -*- coding: utf-8 -*-
 
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

    y = 2.
    for k in range(1,n+1):
        u = 4*k*k
        y = y*u/(u-1)
    return y

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
