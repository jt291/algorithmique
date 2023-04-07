# -*- coding: utf-8 -*-
 
from turtle import *

#-----------------------------------------------------------------------
def p(n,d):
    """
    >>> up(); goto(-150,-150); down(); p(0,300)
    >>> up(); goto(-150,-75); down(); p(1,300)
    >>> up(); goto(-150,0); down(); p(2,300)
    >>> up(); goto(-150,75); down(); p(3,300)
    """
    assert type(n) is int
    assert n >= 0
    if n == 0: forward(d)
    else:
        p(n-1,d/3.)
        left(60)
        p(n-1,d/3.)
        right(120)
        p(n-1,d/3.)
        left(60)
        p(n-1,d/3.)
    return

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
