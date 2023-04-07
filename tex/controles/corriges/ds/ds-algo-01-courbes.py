# -*- coding: utf-8 -*-
 
from math import *

#-----------------------------------------------------------------------
def parametric_circle(x0,y0,r):
    """
    cercle paramétrique : x = x0 + r*cos(t), y = y0 + r * sin(t)
    """
    return lambda t: x0 + r * cos(t), lambda t: y0 + r * sin(t)

#-----------------------------------------------------------------------
def drawCurve(f,t1,t2,dt):
    """
    trace une courbe paramétrée pour t dans [t1,t2] par pas de dt
    pour les fonctions x = f[0](t) et y = f[1](t)
    >>> drawCurve(parametric_circle(-150,0,100),0.,2*pi,0.1)
    >>> drawCurve(parametric_circle(-200,0,50),0.,pi,0.1)
    """
    assert type(t1) is float and type(t2) is float and type(dt) is float
    assert type(f) is tuple
    
    from turtle import up, down, goto
    values = []
    t = t1
    while t < t2:
        values.append(t)
        t = t + dt

    up()
    goto(f[0](t1),f[1](t1))
    down()
    
    for t in values: goto(f[0](t),f[1](t))

    return

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
