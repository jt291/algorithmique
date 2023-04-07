# -*- coding: utf-8 -*-
 
# file (structure FIFO : first in first out) :
# on enfile au début et défile à la fin de la liste
# qui stocke les éléments de la file

#-----------------------------------------------------------------------
def emptyQueue(p):
    """
    ok = emptyQueue(p)
    True si p est une liste vide, False sinon

    >>> emptyQueue([])
    True
    >>> emptyQueue([[]])
    False
    >>> emptyQueue([1,2,3])
    False
    """
    assert type(p) is list

    return (p == [])

#-----------------------------------------------------------------------
def topQueue(p):
    """
    x = topQueue(p)
    tête d'une file p non vide (not emptyQueue(p))

    >>> topQueue([[]])
    []
    >>> topQueue([1,2,3])
    3
    """
    assert not emptyQueue(p)

    return p[len(p)-1]

#-----------------------------------------------------------------------
def pushQueue(p,x):
    """
    pushQueue(p,x) enfile x dans la file p

    >>> p = []; pushQueue(p,2); print(p)
    [2]
    >>> p = [1,2,3]; pushQueue(p,2); print(p)
    [2, 1, 2, 3]
    >>> p = [[]]; pushQueue(p,2); print(p)
    [2, []]
    """
    assert type(p) is list

    p.insert(0,x)
    
    return

#-----------------------------------------------------------------------
def popQueue(p):
    """
    x = popQueue(p) défile le sommet x d'une file p non vide

    >>> p = [1,2,3]; popQueue(p); print(p)
    3
    [1, 2]
    >>> p = [[]]; popQueue(p); print(p)
    []
    []
    """
    assert not emptyQueue(p)

    x = topQueue(p)
    del p[len(p)-1]

    return x

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
