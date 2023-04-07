# -*- coding: utf-8 -*-
 
from math import *

# cosinus directeurs
x, y, z = 1, 1, sqrt(2)
r = sqrt(x*x + y*y + z*z)
a1 = x/r
a2 = y/r
a3 = z/r
print('cosinus directeurs :',x,y,z,'->',a1,a2,a3)

# produit scalaire
x1, y1, z1 = 1, 1, 1
x2, y2, z2 = -1, -1, 2
p = x1*x2 + y1*y2 + z1*z2
print('produit scalaire :',x1,y1,z1,x2,y2,z2,'->',p)

# produit vectoriel
x1, y1, z1 = 1, 1, 1
x2, y2, z2 = -1, -1, 1
x3 = y1*z2 - z1*y2
y3 = z1*x2 - x1*z2
z3 = x1*y2 - y1*x2
print('produit vectoriel :',x1,y1,z1,x2,y2,z2,'->',x3,y3,z3)

# produit mixte
x1, y1, z1 = 1, 1, 1
x2, y2, z2 = -1, -1, 1
v = (y1*z2 - z1*y2)*x3 + (z1*x2 - x1*z2)*y3 + (x1*y2 - y1*x2)*z3
print('produit mixte :',x1,y1,z1,x2,y2,z2,'->',v)
