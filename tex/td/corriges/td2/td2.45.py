# -*- coding: utf-8 -*-
 
from math import *

# zéro d'une fonction : méthode par dichotomie
x1 = 1.
x2 = 2.
s = 1.e-9
f = cos

while (x2 - x1) > s :
    x = (x1 + x2)/2. 
    if f(x1)*f(x) < 0 : x2 = x
    else : x1 = x
print(x, cos(x))


# zéro d'une fonction : méthode des tangentes
x1 = 1.
x2 = 2.
s = 1.e-9
f = cos

df = sin
x = x2 - f(x2)/(-df(x2))
while fabs(x-x2) > s :
    x2 = x
    x = x - f(x)/(-df(x))
print(x, cos(x))

# zéro d'une fonction : méthode des sécantes
x1 = 1.
x2 = 2.
s = 1.e-9
f = cos

df = (f(x2)-f(x1))/(x2-x1)
x = x2 - f(x2)/df
while fabs(x-x2) > s :
    x2 = x
    df = (f(x2)-f(x1))/(x2-x1)
    x = x - f(x)/df
print(x, cos(x))

# zéro d'une fonction : méthode des cordes
x1 = 1.
x2 = 2.
s = 1.e-9
f = cos
while (x2-x1) > s :
    x = (x2*f(x1) - x1*f(x2))/(f(x1)-f(x2))
    if f(x1)*f(x) < 0 : x2 = x
    else : x1 = x
print(x, cos(x))

