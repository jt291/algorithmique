# -*- coding: utf-8 -*-
 
from math import *

x = pi/2

k = 0
terme = x
somme = terme
s = 1.e-9
while fabs(terme) > s:
    terme = -terme*x*x/((2*k+2)*(2*k+3))
    somme = somme + terme
    k = k + 1
print('sin :',x,somme,':',sin(x))
