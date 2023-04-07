# -*- coding: utf-8 -*-
 
def rechercheTout(t,x):
    """
    occurs = rechercheTout(t,x)
    liste des indices de toutes les occurences de x dans la liste t
    
    >>> rechercheTout([1,2,1,5,1],1)
    [0, 2, 4]
    >>> rechercheTout([1,2,1,5,1],2)
    [1]
    >>> rechercheTout([1,2,1,5,1],3)
    []
    """
    assert type(t) is list
    occurs = []
    for i in range(len(t)):
        if t[i] == x: occurs.append(i)
    return occurs

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
