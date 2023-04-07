# -*- coding: utf-8 -*-
 
def f(x):
    y = x + 2
    return y

def g(z):
    v = 2*f(z)
    return v

def h(a):
    b = g(f(a))
    return b

# appels équivalents
t = 2
# u = f(t)
x = t
y = x + 2
tmp = y
del x, y
u = tmp
del tmp
print(t,u,f(t))

# u = g(t)
z = t
x = z
y = x + 2
tmp = y
del x, y
v = 2*tmp
tmp = v
del v, z
u = tmp
del tmp
print(t,u,g(t))

# u = h(t)
a = t
x = a
y = x + 2
tmp = y
del x, y
z = tmp
del tmp
x = z
y = x + 2
tmp = y
del x, y
v = 2*tmp
tmp = v
del v, z
b = tmp
del tmp
tmp = b
del a, b
u = tmp
del tmp
print(t,u,h(t))
