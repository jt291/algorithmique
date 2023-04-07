# -*- coding: utf-8 -*-
 
def coefficientBinome(n,p):
    """
    c = coefficientBinome(n,p)
    p-ième coefficient du binôme (a+b)**n

    >>> n = 6
    >>> for i in range(0,n+1):
    ...     for p in range(0,i+1):
    ...             print(coefficientBinome(i,p),end=' ')
    ...     print()
    ...          
    1 
    1 1 
    1 2 1 
    1 3 3 1 
    1 4 6 4 1 
    1 5 10 10 5 1 
    1 6 15 20 15 6 1 
    """
    assert type(n) is int and type(p) is int
    assert n >= 0 and p >= 0 and p <= n
    
    if p == 0 or n == 0 or n == p:
        return 1
    else:
        return coefficientBinome(n-1,p) + coefficientBinome(n-1,p-1)


#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
