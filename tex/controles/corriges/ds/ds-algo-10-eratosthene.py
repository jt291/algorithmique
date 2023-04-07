# -*- coding: utf-8 -*-
 
def f(t):
    assert type(t) is list
    i = 0
    while i < len(t):
        j = i + 1
        while j < len(t):
            if t[j]%t[i] == 0 : del t[j]
            else: j = j + 1
            print(i, j, t)
        i = i + 1
    return t

#-----------------------------------------------------------------------
f(list(range(2,10)))
