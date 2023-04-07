# -*- coding: utf-8 -*-
 
from turtle import *

#-----------------------------------------------------------------------
def polygone(n,d,x=0,y=0):
    """
    trace un polygone régulier à n côtés de longueur d
    à partir du point de coordonnées (x,y)

    >>> for i in range(3,10): polygone(i,100,-150,0)
    """
    up()
    goto(x,y)
    down()
    for i in range(n):
        forward(d)
        left(360./n)
    return

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
