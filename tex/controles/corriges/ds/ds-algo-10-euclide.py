# -*- coding: utf-8 -*-
 
def f(a,b):
    assert type(a) is int and a >= 0
    assert type(b) is int and b >= 0
    if b == 0 : d = a
    else: d = f(b,a%b)
    print(a, b)
    return d

#-----------------------------------------------------------------------
f(12,18)
