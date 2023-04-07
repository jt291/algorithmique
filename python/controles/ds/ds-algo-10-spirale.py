# -*- coding: utf-8 -*-
 
from turtle import *

#-----------------------------------------------------------------------
def spirale(n,x0,y0,a0,dr):
    """
    spirale(n,x0,y0,a0,dr)
    trace une spirale rectangulaire à n côtés à partir du point de
    coordonnées (x0,y0) et avec une orientation initiale a0.
    dr représente l'incrément de longueur d'un côté de la spirale
    à son suivant immédiat (le premier côté ayant pour longueur dr).
    
    >>> spirale(10,-100,0,0,8)
    >>> spirale(20,0,0,30,3)
    >>> spirale(15,100,0,-45,5)
    """
    assert type(n) is int and n >= 0
    assert type(x0) is int and type(y0) is int
    assert type(a0) is int
    assert type(dr) is int and dr >= 0

    up()
    goto(x0,y0)
    setheading(a0)
    down()

    d = 0
    for i in range(n):
        d = d + dr
        forward(d)
        left(90)
    return

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
