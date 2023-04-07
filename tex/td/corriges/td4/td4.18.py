# -*- coding: utf-8 -*-
 
def triInsertion(t,debut,fin):
    assert type(t) is list
    assert 0 <= debut <= fin < len(t)
    for k in range(debut+1,fin+1):
        i = k - 1
        x = t[k]
        while i >= debut and t[i] > x:
            t[i+1] = t[i]
            i = i - 1
            print(i,k,x,t) # affichage
        t[i+1] = x
    return

triInsertion([9,8,7,6,5,4],1,4)
