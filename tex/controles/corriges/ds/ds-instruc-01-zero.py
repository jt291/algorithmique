# -*- coding: utf-8 -*-
 
from math import *

x1 = 1.
x2 = 2.
s = 1.e-9
f = cos
df = sin

x = x2 - f(x2)/(-df(x2))
while fabs(x-x2) > s:
   x2 = x
   x = x - f(x)/(-df(x))

print(pi/2,x,f(x))
