# -*- coding: utf-8 -*-
 
from math import *

#-----------------------------------------------------------------------
def developpement(x,f,g,k0,u0,y0=0,s=1.0e-9) :
    # calcul de f(x)
    k, u = k0, u0 
    y = y0 + u
    while fabs(u) > s :
        u = g(u,k,x)
        y = y + u
        k = k + 1
    print(f,x,f(x),y)
    return y

#-----------------------------------------------------------------------
# asin(x)
f = asin
x = 0.25
k, u = 0, x
y = 0
g = lambda u,k,x : u*x*x*(2*k+1)*(2*k+1)/((2*k+2)*(2*k+3))
developpement(x,f,g,k,u,y)

# acos(x)
f = acos
x = 0.25
k, u = 0, -x
y = pi/2
g = lambda u,k,x : u*x*x*(2*k+1)*(2*k+1)/((2*k+2)*(2*k+3))
developpement(x,f,g,k,u,y)

# atan(x)
f = atan
x = 0.25
k, u = 0, x
y = 0
g = lambda u,k,x : -u*x*x*(2*k+1)/(2*k+3)
developpement(x,f,g,k,u,y)

# 1/(1+x)
f = lambda x : 1/(1+x)
x = 0.25
k, u = 0, 1
y = 0
g = lambda u,k,x : -u*x
developpement(x,f,g,k,u,y)

# 1/(1-x)
f = lambda x : 1/(1-x)
x = 0.25
k, u = 0, 1
y = 0
g = lambda u,k,x : u*x
developpement(x,f,g,k,u,y)

# 1/(1+x*x)
f = lambda x : 1/(1+x*x)
x = 0.25
k, u = 0, 1
y = 0
g = lambda u,k,x : -u*x*x
developpement(x,f,g,k,u,y)

# 1/(1-x*x)
f = lambda x : 1/(1-x*x)
x = 0.25
k, u = 0, 1
y = 0
g = lambda u,k,x : u*x*x
developpement(x,f,g,k,u,y)

# sqrt(1+x)
f = lambda x : sqrt(1+x)
x = 0.25
k, u = 0, 1
y = 0
g = lambda u,k,x : -u*x*(2*k-1)/(2*(k+1))
developpement(x,f,g,k,u,y)

# 1/sqrt(1+x)
f = lambda x : 1/sqrt(1+x)
x = 0.25
k, u = 0, 1
y = 0
g = lambda u,k,x : -u*x*(2*k+1)/(2*k+2)
developpement(x,f,g,k,u,y)

# 1/sqrt(1-x*x)
f = lambda x : 1/sqrt(1-x*x)
x = 0.25
k, u = 0, 1
y = 0
g = lambda u,k,x : u*x*x*(2*k+1)*(2*k+2)/(4*(k+1)*(k+1))
developpement(x,f,g,k,u,y)

# 1/((a - x)**2)
a = 6/5
f = lambda x : 1/((a - x)**2)
x = 0.25
k, u = 0, 1/(a*a)
y = 0
g = lambda u,k,x : u*x*(k+2)/(a*(k+1))
developpement(x,f,g,k,u,y)

# 1/((a - x)**3)
a = 6/5
f = lambda x : 1/((a - x)**3)
x = 0.25
k, u = 0, 1/(a*a*a)
y = 0
g = lambda u,k,x : u*x*(k+3)/(a*(k+1))
developpement(x,f,g,k,u,y)

# 1/((a - x)**5)
a = 6/5
f = lambda x : 1/((a - x)**5)
x = 0.25
k, u = 0, 1/(a*a*a*a*a)
y = 0
g = lambda u,k,x : u*x*(k+5)/(a*(k+1))
developpement(x,f,g,k,u,y)

# exp(x)
f = exp
x = 0.25
k, u = 0, 1
y = 0
g = lambda u,k,x : u*x/(k+1)
developpement(x,f,g,k,u,y)

# exp(-x)
f = lambda x : exp(-x)
x = 0.25
k, u = 0, 1
y = 0
g = lambda u,k,x : -u*x/(k+1)
developpement(x,f,g,k,u,y)

# log(1+x)
f = lambda x : log(1+x)
x = 0.25
k, u = 1, x
y = 0
g = lambda u,k,x : -u*x*k/(k+1)
developpement(x,f,g,k,u,y)

# log(1-x)
f = lambda x : log(1-x)
x = 0.25
k, u = 1, -x
y = 0
g = lambda u,k,x : u*x*k/(k+1)
developpement(x,f,g,k,u,y)

# log((1+x)/(1-x))
f = lambda x : log((1+x)/(1-x))
x = 0.25
k, u = 1, 2*x
y = 0
g = lambda u,k,x : u*x*x*(2*k+1)/(2*k+3)
developpement(x,f,g,k,u,y)

# sinh(x)
f = sinh
x = 0.25
k, u = 0, x
y = 0
g = lambda u,k,x : u*x*x/((2*k+2)*(2*k+3))
developpement(x,f,g,k,u,y)

# cosh(x)
f = cosh
x = 0.25
k, u = 0, 1
y = 0
g = lambda u,k,x : u*x*x/((2*k+1)*(2*k+2))
developpement(x,f,g,k,u,y)

# asinh(x)
f = asinh
x = 0.25
k, u = 0, x
y = 0
g = lambda u,k,x : -u*x*x*(2*k+1)*(2*k+1)/((2*k+2)*(2*k+3))
developpement(x,f,g,k,u,y)

# atanh(x)
f = atanh
x = 0.25
k, u = 0, x
y = 0
g = lambda u,k,x : u*x*x*(2*k+1)/(2*k+3)
developpement(x,f,g,k,u,y)

# sin(x)
f = sin
x = 0.25
k, u = 0, x
y = 0
g = lambda u,k,x : -u*x*x/((2*k+2)*(2*k+3))
developpement(x,f,g,k,u,y)

# cos(x)
f = cos
x = 0.25
k, u = 0, 1
y = 0
g = lambda u,k,x : -u*x*x/((2*k+1)*(2*k+2))
developpement(x,f,g,k,u,y)
