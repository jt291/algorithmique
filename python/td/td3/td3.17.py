# -*- coding: utf-8 -*-
 
def puissance(x,n):
    """"
    y = puissance(x,n)
    est la puissance entière de x de degré n

    >>> puissance(3,2)
    9
    >>> puissance(2,3)
    8
    >>> puissance(4,0)
    1
    """
    assert type(n) is int and n >= 0
    if n == 0:
        return 1
    else:
        return x*puissance(x,n-1)

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
