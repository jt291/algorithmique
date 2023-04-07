# -*- coding: utf-8 -*-
 
from math import *

x1 = 4.
x2 = 5.
s = 1.e-9
f = cos
df = sin

x = x2 - f(x2)/(-df(x2))
while fabs(x-x2) > s:
   x2 = x
   x = x - f(x)/(-df(x))

print(3*pi/2,x,f(x))

