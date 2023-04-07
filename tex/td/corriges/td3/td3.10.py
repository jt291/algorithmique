# -*- coding: utf-8 -*-
 
# pgcd
def pgcd(a,b):
    """
    d = pgcd(a,b)
    plus grand commun diviseur des 2 entiers a et b

    >>> pgcd(12,18)
    6
    >>> pgcd(18,12)
    6
    >>> pgcd(21,15)
    3
    >>> pgcd(5,7)
    1
    """
    assert type(a) is int and a >= 0
    assert type(b) is int and b >= 0

    if b == 0:
        return a
    else:
        return pgcd(b,a%b)

# ppcm
def ppcm(a,b):
    """
    m = ppcm(a,b)
    plus petit commun multiple de 2 entiers a et b

    >>> ppcm(12,18)
    36
    >>> ppcm(18,12)
    36
    >>> ppcm(21,15)
    105
    >>> ppcm(5,7)
    35
    >>> ppcm(0,6)
    0
    """
    assert type(a) is int and a >= 0
    assert type(b) is int and b >= 0

    if a == 0 or b == 0:
        return 0
    else:
        return a*b//pgcd(a,b)

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
