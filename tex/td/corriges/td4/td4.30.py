# -*- coding: utf-8 -*-
 
def mesureRecherche(f,t,x):  
    t0 = time()
    f(tmp,x,0,len(t)-1)
    dt = time() - t0
    return dt

"""
>>> s = liste(1000)
>>> x = s[len(s)-1]
>>> mesureRecherche(rechercheSequentielle,s,x)
0.00062489509582519531
>>> s = liste(100000)
>>> x = s[len(s)-1]
>>> mesureRecherche(rechercheSequentielle,s,x)
0.046545028686523438
"""
