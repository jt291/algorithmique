# -*- coding: utf-8 -*-
 
def calculPi(n):
    """
    y = calculPi(n)
    calcul de pi à l'ordre n
    >>> from math import fabs, pi
    >>> fabs(pi - calculPi(0)) < 1.e0
    True
    >>> fabs(pi - calculPi(1)) < 1.e-1
    True
    >>> fabs(pi - calculPi(2)) < 1.e-2
    True
    >>> fabs(pi - calculPi(5)) < 1.e-5
    True
    >>> fabs(pi - calculPi(10)) < 1.e-10
    True
    >>> fabs(pi - calculPi(100)) < 1.e-100
    True
    """
    assert type(n) is int and n >= 0

    u = 1.
    y = 4./1. - 2./4. - 1./5. - 1./6.
    for k in range(1,n+1):
        u = u/16.
        y = y + u*(4./(8*k + 1) - 2./(8*k + 4) - 1./(8*k + 5) - 1./(8*k + 6))

    return y

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
