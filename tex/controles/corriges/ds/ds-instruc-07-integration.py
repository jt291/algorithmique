# -*- coding: utf-8 -*-
 
from math import *

f = sin
a = 0.
b = pi
n = 100000
I = 0.0
largeur = (b-a)/n
x = a + largeur/2
while x < b:
    I = I + f(x)
    x = x + largeur
I = I*largeur

print(I-2)
