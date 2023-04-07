# -*- coding: utf-8 -*-
 
from math import *

n = 100000

y = 0.
for k in range(1,n+1):
    y = y + 1./(k*k)

print(pi-sqrt(6*y))
