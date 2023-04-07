# -*- coding: utf-8 -*-
 
def f(t):
    assert type(t) is list

    for i in range(len(t)):
        m = i
        for j in range(i+1,len(t)):
            if t[j] > t[m]: m = j
        t[i],t[m] = t[m],t[i]
        print(i, t)  #---------- affichage

    return t

#----------------------------------------
f([5,1,4,7,10])
