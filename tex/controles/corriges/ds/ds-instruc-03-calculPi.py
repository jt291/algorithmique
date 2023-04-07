# -*- coding: utf-8 -*-
 
from math import *

n = 100000

y = 2.
for k in range(1,n+1):
    y = y*(4*k*k)/(4*k*k-1)

print(pi - y)

