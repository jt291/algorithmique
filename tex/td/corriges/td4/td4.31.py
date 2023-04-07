# -*- coding: utf-8 -*-
 
def mesureTri(f,t):
    tmp = [x for x in t]
    t0 = time()
    f(tmp,0,len(t)-1)
    dt = time() - t0
    return dt

"""
>>> s = liste(10000)
>>> mesureTri(triSelection,s)
23.040315866470337
>>> mesureTri(triInsertion,s)
22.086866855621338
>>> mesureTri(triRapide,s)
0.24324798583984375
"""
