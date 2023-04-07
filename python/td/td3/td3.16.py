# -*- coding: utf-8 -*-
 
def sommeGeometrique(n,a,b):
    """
    s = sommeGeometrique1(n,a,b)
    somme des n premiers termes d'une suite géométrique
    uk = a*b**k

    >>> sommeGeometrique(5,1,2)
    63
    >>> sommeGeometrique(5,1,3)
    364
    """
    assert type(a) is int and a != 0
    assert type(b) is int and b != 1
    assert type(n) is int and n >= 0

    if n == 0:
        return 1
    else:
        return sommeGeometrique(n-1,a,b) + (a * b**n)

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
