# -*- coding: utf-8 -*-
 
def motif(t,m,debut,fin):
    """
    ok, i = motif(t,m,debut,fin)
    ok == True : i est l'indice de la première occurence
    du motif m dans la liste t entre les indices debut et fin
    ok == False : le motif m n'a pas été trouvé dans la liste t
    
    >>> motif([1,2,3,2,3,4],[2,4],0,5)
    (False, 5)
    >>> motif([1,2,3,2,3,4],[2,3],0,5)
    (True, 1)
    >>> motif([1,2,3,2,3,4],[2,3],2,5)
    (True, 3)
    >>> motif([1,2,3,2,3,4],[2,3,4],0,5)
    (True, 3)
    """
    assert type(t) is list
    assert type(m) is list
    assert 0 <= debut <= fin < len(t)
    
    i,ok = debut,False
    while i + len(m) - 1 <= fin and not ok:
        if t[i:i+len(m)] == m and m != []:
            ok = True
        else: i = i + 1
    return ok,i

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
