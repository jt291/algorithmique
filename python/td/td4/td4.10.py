# -*- coding: utf-8 -*-
 
# pile (structure LIFO : last in first out) :
# on empile et dépile à la fin de la liste
# qui stocke les éléments de la pile

#-----------------------------------------------------------------------
def emptyStack(p):
    """
    ok = emptyStack(p)
    True si p est une liste vide, False sinon

    >>> emptyStack([])
    True
    >>> emptyStack([[]])
    False
    >>> emptyStack([1,2,3])
    False
    """
    assert type(p) is list

    return (p == [])

#-----------------------------------------------------------------------
def topStack(p):
    """
    x = topStack(p)
    sommet d'une pile p non vide (not emptyStack(p))

    >>> topStack([[]])
    []
    >>> topStack([1,2,3])
    3
    """
    assert not emptyStack(p)

    return p[len(p)-1]

#-----------------------------------------------------------------------
def pushStack(p,x):
    """
    pushStack(p,x) empile x sur le sommet de la pile p

    >>> p = []; pushStack(p,2); print(p)
    [2]
    >>> p = [1,2,3]; pushStack(p,2); print(p)
    [1, 2, 3, 2]
    >>> p = [[]]; pushStack(p,2); print(p)
    [[], 2]
    """
    assert type(p) is list

    p.append(x)
    
    return

#-----------------------------------------------------------------------
def popStack(p):
    """
    x = popStack(p) dépile le sommet x d'une pile p non vide

    >>> p = [1,2,3]; popStack(p); print(p)
    3
    [1, 2]
    >>> p = [[]]; popStack(p); print(p)
    []
    []
    """
    assert not emptyStack(p)

    x = topStack(p)
    del p[len(p)-1]

    return x

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
