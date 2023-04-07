# -*- coding: utf-8 -*-
 
def h(x):
    assert type(x) is int
    
    return x%2 == 0

#----------------------------------------
def g(p,t):
    assert type(t) is list

    i = 0
    while i < len(t):
        if p(t[i]) == True:
            del t[i]
        else: i = i + 1
        print(i, t)  #---------- affichage
    return t


#----------------------------------------
g(h,[5,1,4,7,10])
