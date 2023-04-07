# -*- coding: utf-8 -*-
 
def f(x):
    x = 2*x
    print('f', x)
    return x

def g(x):
    x = 2*f(x)
    print('g', x)
    return x

def h(x):
    x = 2*g(f(x))
    print('h', x)
    return x

x = 5
print(x)
print('---')
y = f(x)
print(x)
print('---')
z = g(x)
print(x)
print('---')
t = h(x)
print(x)
print('---')
print()

x = 5
print(x)
print('---')
x = f(x)
print(x)
print('---')
x = g(x)
print(x)
print('---')
x = h(x)
print(x)
