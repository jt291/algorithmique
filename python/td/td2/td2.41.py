# -*- coding: utf-8 -*-
 
from math import *

x = 0.25

# développement limité 1 : sinh(x)
k = 0
u = x
y = u
s = 1.e-6
while fabs(u) > s :
    u = u*x*x/((2*k+2)*(2*k+3))
    y = y + u
    k = k + 1
print('sinh   :',x,s,'->',y,':',sinh(x))

# développement limité 2 : cosh(x)
k = 0
u = 1.
y = u
s = 1.e-6
while fabs(u) > s :
    u = u*x*x/((2*k+1)*(2*k+2))
    y = y + u
    k = k + 1
print('cosh   :',x,s,'->',y,':',cosh(x))

# développement limité 3 : cos(x)
k = 0
u = 1.
y = u
s = 1.e-6
while fabs(u) > s :
    u = -u*x*x/((2*k+1)*(2*k+2))
    y = y + u
    k = k + 1
print('cos    :',x,s,'->',y,':',cos(x))

# développement limité 4 : log(1+x)
if fabs(x) < 1 :
    k = 0
    u = x
    y = u
    s = 1.e-6
    while fabs(u) > s :
        u = -u*x*(k+1)/(k+2)
        y = y + u
        k = k + 1
print('log    :',x,s,'->',y,':',log(1+x))

# développement limité 5 : arctan(x)
if fabs(x) < 1 :
    k = 0
    u = x
    y = u
    s = 1.e-6
    while fabs(u) > s :
        u = -u*x*x*(2*k+1)/(2*k+3)
        y = y + u
        k = k + 1
print('arctan :',x,s,'->',y,':',atan(x))
