# -*- coding: utf-8 -*-
 
a, b, c = 0, 1, 0
u = a and c
v = b and not c
s = u or v
print(a,b,c,'->',int(s))
