# -*- coding: utf-8 -*-
 
# suite géométrique 1 : version constante
# complexité indépendante de n

def sommeGeometrique1(n,a,b) :
    """
    s = sommeGeometrique1(n,a,b)
    somme des n premiers termes d'une suite géométrique
    uk = a*b**k

    >>> sommeGeometrique1(5,1,2)
    63
    >>> sommeGeometrique1(5,1,3)
    364
    """
    assert type(a) is int and a != 0
    assert type(b) is int and b != 1
    assert type(n) is int and n >= 0

    s = a*(b**(n+1) - 1)//(b-1)

    return s

# suite géométrique 2 : version itérative
# complexité linéaire O(n)

def sommeGeometrique2(n,a,b) :
    """
    s = sommeGeometrique2(n,a,b)
    somme des n premiers termes d'une suite géométrique
    uk = a*b**k

    >>> sommeGeometrique2(5,1,2)
    63
    >>> sommeGeometrique2(5,1,3)
    364
    """
    assert type(a) is int and a != 0
    assert type(b) is int and b != 1
    assert type(n) is int and n >= 0

    s = 0
    for i in range(n+1):
        s = s + a*b**i

    return s

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
