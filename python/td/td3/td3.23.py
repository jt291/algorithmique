# -*- coding: utf-8 -*-
 
from math import *

# intégration 1 : méthode des rectangles
def rectangle_integration(f,x1,x2,n):
    """
    intégration de f(x) entre x1 et x2
    par la méthode des n rectangles

    >>> fabs(rectangle_integration(sin,0.,2*pi,100000)) < 1.e-5
    True
    >>> fabs(rectangle_integration(sin,0.,pi,100000) - 2.) < 1.e-5
    True
    >>> fabs(rectangle_integration(sin,0.,pi/2,100000) - 1) < 1.e-5
    True
    >>> fabs(rectangle_integration(cos,0.,pi,100000)) < 1.e-5
    True
    >>> fabs(rectangle_integration(cos,-pi/2,pi/2,100000) - 2) < 1.e-5
    True
    """
    assert type(x1) is float
    assert type(x2) is float
    assert x1 <= x2

    integral = 0.0
    width = (x2 - x1)/n
    x = x1 + width/2
    while x < x2:
        integral = integral + f(x)
        x = x + width
    integral = integral*width
    return integral

# intégration 2 : méthode des trapèzes
def trapezoid_integration(f,x1,x2,n):

    """
    intégration de f(x) entre x1 et x2
    par la méthode des n trapèzes

    >>> fabs(trapezoid_integration(sin,0.,2*pi,100000)) < 1.e-5
    True
    >>> fabs(trapezoid_integration(sin,0.,pi,100000) - 2.) < 1.e-5
    True
    >>> fabs(trapezoid_integration(sin,0.,pi/2,100000) - 1) < 1.e-4
    True
    >>> fabs(trapezoid_integration(cos,0.,pi,100000)) < 1.e-4
    True
    >>> fabs(trapezoid_integration(cos,-pi/2,pi/2,100000) - 2) < 1.e-5
    True
    """
    assert type(n) is int
    assert type(x1) is float
    assert type(x2) is float
    assert x1 <= x2

    integral = (f(x1) + f(x2))/2
    width = (x2 - x1)/n
    x = x1 + width
    while x < x2:
        integral = integral + f(x)
        x = x + width
    integral = integral*width
    return integral

# intégration 3 : méthode de Simpson
def simpson_integration(f,x1,x2,n):
    """
    intégration de f(x) entre x1 et x2
    par la méthode de Simpson

    >>> fabs(simpson_integration(sin,0.,2*pi,100000)) < 1.e-5
    True
    >>> fabs(simpson_integration(sin,0.,pi,100000) - 2.) < 1.e-5
    True
    >>> fabs(simpson_integration(sin,0.,pi/2,100000) - 1) < 1.e-5
    True
    >>> fabs(simpson_integration(cos,0.,pi,100000)) < 1.e-5
    True
    >>> fabs(simpson_integration(cos,-pi/2,pi/2,100000) - 2) < 1.e-5
    True
    """
    assert type(n) is int
    assert type(x1) is float
    assert type(x2) is float
    assert x1 <= x2
    assert n%2 == 0

    integral = f(x1) + f(x2)
    width = (x2 - x1)/n
    for i in range(1,n,2):
        integral = integral + 4*f(x1 + i*width)
    for i in range(2,n,2):
        integral = integral + 2*f(x1 + i*width)
    integral = integral*width/3
    return integral

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
