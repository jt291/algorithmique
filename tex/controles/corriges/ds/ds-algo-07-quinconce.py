# -*- coding: utf-8 -*-
 
from turtle import *

#-----------------------------------------------------------------------
def quinconce(n,m,r):
    """
    quinconce(n,m,r)
    trace n rangées de m cercles de rayon r
    disposés en quinconce
    >>> quinconce(5,10,10)
    """
    assert type(n) is int and n > 0
    assert type(m) is int and m > 0
    assert type(r) is int and r > 0
    
    for i in range(n) :
        x0 = r*(i%2)
        y0 = 2*i*r
        for j in range(m) :
            up()
            goto(x0+2*j*r,y0)
            down()
            circle(r)           
    return

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
