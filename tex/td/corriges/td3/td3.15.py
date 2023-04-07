# -*- coding: utf-8 -*-
 
def f(x):
    x = x + 2
    print('f', x)
    return x

def g(x):
    x = 2*f(x)
    print('g', x)
    return x

def h(x):
    x = g(f(x))
    print('h', x)
    return x

x = 5
print(x)
print('---')
x = x + 2
print(x)
print('---')
x = 2 * (x + 2)
print(x)
print('---')
print()

x = 5
print(x)
print('---')
y = f(x)
print(x, y)
print('---')
z = 2*f(y)
print(x, y, z)
print('---')
print()

x = 5
print(x)
print('---')
z = 2*f(f(x))
print(x, z)
print('---')
print()

x = 5
print(x)
print('---')
f(x)
print('---')
print(x)
print('---')
g(x)
print('---')
print(x)
print('---')
h(x)
print('---')
print(x)
print('---')
print()
