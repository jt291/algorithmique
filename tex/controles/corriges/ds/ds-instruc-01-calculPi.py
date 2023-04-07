# -*- coding: utf-8 -*-
 
from math import *

n = 100000

y = 0.
for k in range(0,n+1) :
    y = y + sqrt(1 - (1.*k*k)/(n*n))

print(pi - 4*y/n)


