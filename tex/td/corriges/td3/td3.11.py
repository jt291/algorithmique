# -*- coding: utf-8 -*-
 
# somme arithmétique 1 : version constante
def sommeArithmetique1(a,b,n):
    """
    s = sommeArithmetique1(a,b,n)
    somme des n premiers termes d'une suite arithmétique
    uk = a + b*k

    >>> sommeArithmetique1(0,1,5)
    15
    >>> sommeArithmetique1(0,1,6)
    21
    >>> sommeArithmetique1(1,1,6)
    28
    >>> sommeArithmetique1(1,2,6)
    49
    """
    assert type(a) is int and a >= 0
    assert type(b) is int and b >= 0
    assert type(n) is int and n >= 0
    
    s = a*(n+1) + b*n*(n+1)//2

    return s


# somme arithmétique 2 : version itérative
def sommeArithmetique2(a,b,n):
    """
    s = sommeArithmetique2(a,b,n)
    somme des n premiers termes d'une suite arithmétique
    uk = a + b*k

    >>> sommeArithmetique2(0,1,5)
    15
    >>> sommeArithmetique2(0,1,6)
    21
    >>> sommeArithmetique2(1,1,6)
    28
    >>> sommeArithmetique2(1,2,6)
    49
    """
    assert type(a) is int and a >= 0
    assert type(b) is int and b >= 0
    assert type(n) is int and n >= 0
    
    s = 0
    for i in range(n+1):
        s = s + a + b*i

    return s

# somme arithmétique 3 : version récursive
def sommeArithmetique3(a,b,n):
    """
    s = sommeArithmetique3(a,b,n)
    somme des n premiers termes d'une suite arithmétique
    uk = a + b*k

    >>> sommeArithmetique3(0,1,5)
    15
    >>> sommeArithmetique3(0,1,6)
    21
    >>> sommeArithmetique3(1,1,6)
    28
    >>> sommeArithmetique3(1,2,6)
    49
    """
    assert type(a) is int and a >= 0
    assert type(b) is int and b >= 0
    assert type(n) is int and n >= 0
    
    if n == 0:
        return a
    else:
        return (a + b*n) + sommeArithmetique3(a,b,n-1)

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
