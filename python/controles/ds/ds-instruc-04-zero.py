# -*- coding: utf-8 -*-
 
from math import *

a, b = 3., 4.
s = 1.e-9
f = cos

while (b - a) > s:
   x = (b*f(a) - a*f(b))/(f(a)-f(b))
   if f(a)*f(x) < 0: b = x
   else: a = x

print(3*pi/2,x,f(x))

