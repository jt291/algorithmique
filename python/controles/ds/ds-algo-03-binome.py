# -*- coding: utf-8 -*-
 
def f(n):
    for p in range(n+1) :
        num = 1
        den = 1
        for i in range(1,p+1) :
            num = num*(n-i+1)
            den = den*i
        c = num//den
        print(c,end=' ')    #------------ affichage
    print()                 #------------ affichage
    return

#-----------------------------------------------------------------------
for n in range(7): f(n)

