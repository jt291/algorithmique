# -*- coding: utf-8 -*-
 
def decodage(code,b):
    """
    n = decodage(code,b)
    n est l'entier décimal correspondant au code (liste de chiffres)
    dans la base b

    >>> decodage([1,2,3],5)
    38
    >>> decodage([1,2,3],8)
    83
    >>> decodage([1,2,3],16)
    291
    >>> decodage([1,2,3],10)
    123
    >>> decodage([1,0,11],12)
    155
    """
    assert type(code) is list
    assert type(b) is int and b > 1

    n = 0
    for i in range(len(code)):
        n = n + code[i]*b**(len(code)-1-i)

    return n

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
