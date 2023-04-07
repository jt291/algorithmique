# -*- coding: utf-8 -*-
 
def triBulles(t,debut,fin):
    """
    t = triBulles(t,debut,fin)
    trie la liste t entre les indices debut et fin
    par la méthode du tri par bulles
    
    >>> s = [9,8,7,6,5,4]
    >>> triBulles(s,0,len(s)-1)
    [4, 5, 6, 7, 8, 9]
    >>> s = [9,8,7,6,5,4]
    >>> triBulles(s,1,4)
    [9, 5, 6, 7, 8, 4]
    """
    assert type(t) is list
    assert 0 <= debut <= fin < len(t)
    
    while debut < fin:
        for j in range(fin,debut,-1):
            if t[j] < t[j-1]: 
                t[j],t[j-1] = t[j-1],t[j]
        debut = debut + 1
        
    return t

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
