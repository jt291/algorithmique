# -*- coding: utf-8 -*-
 
from math import *

n = 100000

y = 2.
for k in range(1,n+1):
    u = 4*k*k
    y = y * u/(u-1)

print(pi-y)

