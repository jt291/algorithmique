# -*- coding: utf-8 -*-
 
a, b = 18, 7

q, r = 0, a
while r > b :
    r = r - b
    q = q + 1
print(a,b,'->',q,r)
