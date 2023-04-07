# -*- coding: utf-8 -*-
 
from math import *

a, b = 3., 4.
s = 1.e-9
f = sin

x = (a + b)/2
while (b - a) > s:
   if f(a)*f(x) < 0 : b = x
   else : a = x
   x = (a + b)/2

print(pi,x,f(x))

