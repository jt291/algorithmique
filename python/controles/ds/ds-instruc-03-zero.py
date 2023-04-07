# -*- coding: utf-8 -*-
 
from math import *

a = 3.
b = 4.
s = 1.e-9
f = sin
df = cos

x = b - f(b)/df(b)
while fabs(x-b) > s:
   b = x
   x = x - f(x)/(df(x))

print(pi,x,f(x))

