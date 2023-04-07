# -*- coding: utf-8 -*-
 
from math import *

a, b, c = 1, 0, -1

delta = b*b - 4*a*c
if delta > 0 :
    racines = [(-b - sqrt(delta))/(2*a), (-b + sqrt(delta))/(2*a)]
elif delta == 0 :
    racines = [-b/(2*a)]
else :
    racines = []

print(a,b,c,':',racines)
