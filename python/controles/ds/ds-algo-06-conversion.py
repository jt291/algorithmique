# -*- coding: utf-8 -*-
 
def conversion(code,b=2):
    """
    n = conversion(code,b)
    entier décimal qui représente le code en base b
    
    >>> conversion([0,0,1,0,1,1,1],2)
    23
    >>> conversion([0, 0, 0, 4, 3],5)
    23
    >>> conversion([1,2],21)
    23
    >>> conversion([0,0,0,0,0,23],25)
    23
    """
    assert type(b) is int and b > 1
    assert type(code) is list

    n = 0  
    for i in range(len(code)):
        n = n + (b**i)*code[len(code)-1-i]
	
    return n

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
