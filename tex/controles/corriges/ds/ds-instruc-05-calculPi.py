# -*- coding: utf-8 -*-
 
from math import *

n = 100000

u = 1.
y = 1.
for k in range(0,n+1):
    u = -u*(2*k+1)/(2*k+3)
    y = y + u

print(pi-(4*y))

