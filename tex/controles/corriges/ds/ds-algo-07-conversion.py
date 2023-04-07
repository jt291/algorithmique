# -*- coding: utf-8 -*-
 
def conversion(n,b=2,k=8):
    """
    code = conversion(n,b,k)
    code en base b sur k bits de l'entier décimal n -> list
    
    >>> conversion(23,2,8)
    [0, 0, 0, 1, 0, 1, 1, 1]
    >>> conversion(23,5,3)
    [0, 4, 3]
    >>> conversion(23,21,3)
    [0, 1, 2]
    >>> conversion(23,25,2)
    [0, 23]
    """
    assert type(n) is int
    assert type(b) is int
    assert type(k) is int
    assert n >= 0 and b > 1 and k > 0
    assert n < b**k - 1
    
    code = []
    quotient = n
    for i in range(k): code.append(0)
    
    i = k - 1
    while quotient != 0 and i >= 0:
        code[i] = quotient%b
        quotient = quotient//b
        i = i - 1
	
    return code

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
