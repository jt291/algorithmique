# -*- coding: utf-8 -*-
 
from math import *

n = 100000

y = 1.
k = 1
while k <= n:
    k = k + 1
    y = y + 1./(k*k)
y = sqrt(y*6)

print(pi - y)
