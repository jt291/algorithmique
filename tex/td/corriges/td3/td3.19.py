# -*- coding: utf-8 -*-
 
def ackerman(m,n):
    """
    y = ackerman(m,n)
    calcul la fonction d'Ackerman pour le couple d'entiers m,n

    >>> ackerman(0,0)
    1
    >>> ackerman(1,0)
    2
    >>> ackerman(2,0)
    3
    >>> ackerman(0,1)
    2
    >>> ackerman(0,2)
    3
    >>> ackerman(1,1)
    3
    >>> ackerman(1,2)
    4
    >>> ackerman(2,2)
    7
    >>> ackerman(3,3)
    61
   """
    assert type(n) is int and type(m) is int
    assert n >= 0 and m >= 0
    
    if m == 0:
        return n + 1
    elif n == 0:
        return ackerman(m-1,1)
    else:
        return ackerman(m-1,ackerman(m,n-1))

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
