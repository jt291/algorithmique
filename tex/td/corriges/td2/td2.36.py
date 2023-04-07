# -*- coding: utf-8 -*-
 
from math import pi

# rectangle
l, L = 2, 3
p = 2*(L+l)
s = L*l
print('rectangle :',l,L,'->',p,s)

# cercle
r = 1
p = 2*pi*r
s = pi*r*r
print('cercle    :',r,'->',p,s)

# cylindre
r, h = 1, 2
s = 2*pi*r*h
v = pi*r*r*h
print('cylindre  :',r,h,'->',s,v)

# sphère
r = 1
s = 4*pi*r*r
v = 4*pi*r*r*r/3
print('sphère    :',r,'->',s,v)
