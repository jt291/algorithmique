# -*- coding: utf-8 -*-
 
# division entière : a = b*q + r
a = 19
b = 6
q = 0
r = a
print('avant :',a,b,q,r)

r = r - b
q = q + 1
r = r - b
q = q + 1
r = r - b
q = q + 1
print('après :',a,b,q,r)
