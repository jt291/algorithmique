# -*- coding: utf-8 -*-
 
from math import *
from turtle import *

#-----------------------------------------------------------------------
def parametric_line(x0,y0,alpha,beta):
    """
    droite paramétrique
    x = x0 + alpha*t, y = y0 + beta*t
    """
    return lambda t: x0 + alpha*t,\
           lambda t: y0 + beta*t

#-----------------------------------------------------------------------
def parametric_circle(x0,y0,r):
    """
    cercle paramétrique
    x = x0 + r*cos(theta), y = y0 + r * sin(theta)
    """
    return lambda theta: x0 + r * cos(theta),\
           lambda theta: y0 + r * sin(theta)

#-----------------------------------------------------------------------
def parametric_ellipse(x0,y0,a,b):
    """
    ellipse paramétrique
    x = x0 + a*cos(phi), y = y0 + b*sin(phi)
    """
    return lambda phi: x0 + a*cos(phi),\
           lambda phi: y0 + b*sin(phi)

#-----------------------------------------------------------------------
def parametric_hyperbola(x0,y0,a,b):
    """
    hyperbole paramétrique
    x = x0 + a/cos(theta), y = y0 + b*tan(theta)
    """
    return lambda theta: x0 + a/cos(theta),\
           lambda theta: y0 + b*tan(theta)

#-----------------------------------------------------------------------
def parametric_cycloid(x0,y0,r):
    """
    cycloïde paramétrique
    x = x0 + r*(phi-sin(phi)), y = y0 + r*(1-cos(phi))
    """
    return lambda phi: x0 + r*(phi-sin(phi)),\
           lambda phi: y0 + r*(1-cos(phi))

#-----------------------------------------------------------------------
def parametric_epicycloid(x0,y0,R,r):
    """
    épicycloïde paramétrique
    x = x0 + (R+r)*cos(theta) - r*cos(theta*(R+r)/r),
    x = y0 + (R+r)*sin(theta) - r*sin(theta*(R+r)/r)
    """
    return lambda theta: x0 + (R+r)*cos(theta) - r*cos(theta*(R+r)/r),\
           lambda theta: y0 + (R+r)*sin(theta) - r*sin(theta*(R+r)/r)

#-----------------------------------------------------------------------
def parametric_hypercycloid(x0,y0,R,r):
    """
    hypercycloïde paramétrique
    x = x0 + (R-r)*cos(theta) + r*cos(theta*(R-r)/r),
    x = y0 + (R-r)*sin(theta) + r*sin(theta*(R-r)/r)
    """
    return lambda theta: x0 + (R-r)*cos(theta) + r*cos(theta*(R-r)/r),\
           lambda theta: y0 + (R-r)*sin(theta) + r*sin(theta*(R-r)/r)

#-----------------------------------------------------------------------
def pascal_snail(x0,y0,a,b):
    """
    limaçon de Pascal
    x = x0 + (a*cos(theta) + b)*cos(theta)
    y = y0 + (a*cos(theta) + b)*sin(theta)
    """
    return lambda theta: x0 + (a*cos(theta) + b)*cos(theta),\
           lambda theta: y0 + (a*cos(theta) + b)*sin(theta)

#-----------------------------------------------------------------------
def logarithmic_spiral(x0,y0,k):
    """
    spirale logarithmique
    x = x0 + k*exp(theta)*cos(theta)
    y = y0 + k*exp(theta)*sin(theta)
    """
    return lambda theta: x0 + k*exp(theta)*cos(theta),\
           lambda theta: y0 + k*exp(theta)*sin(theta)

#-----------------------------------------------------------------------
def drawCurve(f,t1,t2,dt):
    """
    trace une courbe paramétrée pour t dans [t1,t2] par pas de dt
    pour les fonctions x = fx(t) et y = fy(t) où f = (fx,fy)

    >>> drawCurve(parametric_line(10,-10,2,3),-20.,20.,0.1)
    >>> drawCurve(parametric_circle(10,-20,40),0.,2*pi,pi/100)
    >>> drawCurve(parametric_ellipse(-30.,-10.,70,30),0.,2*pi,pi/100)
    >>> drawCurve(parametric_hyperbola(-50.,0.,70,30),-1.,1.,0.1)
    >>> drawCurve(parametric_cycloid(-150.,-100.,20.),0.,5*pi,pi/100)
    >>> drawCurve(parametric_epicycloid(-100.,75.,40.,4.),0.,2*pi,pi/100)
    >>> drawCurve(parametric_hypercycloid(100.,75.,40.,6.),0.,8*pi,pi/100)
    >>> drawCurve(pascal_snail(-150.,0.,100.,80.),0.,2*pi,pi/100)
    >>> drawCurve(logarithmic_spiral(100.,0.,0.1),0.,7.,pi/50)
    """
    assert type(t1) is float
    assert type(t2) is float
    assert type(dt) is float

    (fx, fy) = f
    values = []
    t = t1 + dt
    while t < t2:
        values.append(t)
        t = t + dt
    up()
    goto(fx(t1),fy(t1))
    down()
    for t in values:
        goto(fx(t),fy(t))
    return

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
