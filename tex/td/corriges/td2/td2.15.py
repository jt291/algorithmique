# -*- coding: utf-8 -*-
 
a, b = 15, 21

L, l = a, b
r = L%l
while r > 0 :
    L = l
    l = r
    r = L%l
print(a,b,'->',l)
