# -*- coding: utf-8 -*-
 

#-----------------------------------------------------------------------
def triRapideIteratif(t,debut,fin):
    assert type(t) is list
    assert 0 <= debut 
    assert fin <= len(t)
    pile = []
    while True:
        while debut < fin:
            pivot = t[debut]
            place = partition(t,debut,fin,pivot)
            empiler(pile,(debut,fin,place))
            fin = place - 1
        if not len(pile) == 0:
            (debut,fin,place) = depiler(pile)
            debut = place + 1
        else: return
    return

#-----------------------------------------------------------------------
def triRapideRecursif(t,debut,fin):
    assert type(t) is list
    assert 0 <= debut 
    assert fin <= len(t)
    if debut < fin:
        pivot = t[debut]
        place = partition(t,debut,fin,pivot)
        triRapideRecursif(t,debut,place-1)
        triRapideRecursif(t,place+1,fin)
    return
    
#-----------------------------------------------------------------------
def partition(t,debut,fin,pivot):
    p,inf,sup = debut,debut,fin;
    while p <= sup:
        if t[p] == pivot: 
            p = p + 1
        elif t[p] < pivot:
            t[inf],t[p] = t[p],t[inf]
            inf = inf + 1
            p = p + 1
        else:
            t[sup],t[p] = t[p],t[sup]
            sup = sup - 1
    if p > 0: p = p - 1
    return p

#-----------------------------------------------------------------------
def empiler(p,x):
    assert type(p) is list
    p.append(x)
    return

#-----------------------------------------------------------------------
def depiler(p):
    assert type(p) is list
    assert len(p) > 0
    x = p[len(p)-1]
    del p[len(p)-1]
    return x

#-----------------------------------------------------------------------
from random import randint
from time import time

for n in [10,100,1000,10000,100000,1000000,10000000] :
    s1, s2 = [], []
    for k in range(n) :
        x = randint(0,10*n)
        s1.append(x)
        s2.append(x)
    t1 = time()
    triRapideRecursif(s1,0,len(s1)-1)
    t2 = time()
    print('récursif :',n,t2-t1)
    t1 = time()
    triRapideIteratif(s2,0,len(s2)-1)
    t2 = time()
    print('itératif :',n,t2-t1)

"""Exemples de temps obtenus :
récursif : 10 0.00011992454528808594
itératif : 10 4.887580871582031e-05
récursif : 100 0.0007030963897705078
itératif : 100 0.0012509822845458984
récursif : 1000 0.010165929794311523
itératif : 1000 0.009513139724731445
récursif : 10000 0.12292003631591797
itératif : 10000 0.13573694229125977
récursif : 100000 1.550318956375122
itératif : 100000 1.585007905960083
récursif : 1000000 18.29716205596924
itératif : 1000000 18.76704502105713
récursif : 10000000 233.44398999214172
itératif : 10000000 243.83070611953735
"""
