# -*- coding: utf-8 -*-
 
def pgcd_ppcm(a,b):
    """
    (pgcd, ppcm) = pgcd_ppcm(a,b)
    plus grand commun diviseur et plus petit commun multiple
    des 2 entiers a et b

    >>> pgcd_ppcm(12,18)
    (6, 36)
    >>> pgcd_ppcm(21,15)
    (3, 105)
    >>> pgcd_ppcm(5,7)
    (1, 35)
    """
    assert type(a) is int and a >= 0
    assert type(b) is int and b >= 0

    n1, n2 = a, b
    while n2 != 0:
        r = n1%n2
        n1 = n2
        n2 = r
    pgcd = n1
    if pgcd == 0: ppcm = 0
    else        : ppcm = a*b//pgcd
    
    return (pgcd,ppcm)

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
