# -*- coding: utf-8 -*-
 
from math import *

p1 = lambda e : e%2 == 0
p2 = lambda e : sqrt(e) == int(sqrt(e))

#-----------------------------------------------------------------------
def selection(s,p):
    """
    t = selection(s,p)
    liste des éléments de la liste s qui vérifient
    la condition p (p(s[i]) == True)

    >>> selection([0,1,2,3,4,5,6],p1)
    [0, 2, 4, 6]
    >>> selection([2,4,6,9],p2)
    [4, 9]
    """
    assert type(s) is list

    t = []
    for e in s:
        if p(e) == True :
            t.append(e)

    return t

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
