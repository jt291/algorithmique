# -*- coding: utf-8 -*-
 
def recherchePremier(t,x,debut):
    """
    ok,index = recherchePremier(t,x,debut)
    recherche la première occurence de x dans la liste t en commençant
    à l'indice debut
    ok == True si x a été trouvé à l'indice index, False sinon

    >>> recherchePremier([3,6,1,4,1,5,2,4],1,0)
    (True, 2)
    >>> recherchePremier([3,6,1,4,1,5,2,4],1,3)
    (True, 4)
    >>> recherchePremier([3,6,1,4,1,5,2,4],1,5)
    (False, 8)
    """
    assert type(t) is list
    assert type(debut) is int and 0 <= debut <= len(t)

    ok, index = False, debut
    if index > len(t) - 1: ok = False
    else:
        if t[index] == x: ok = True
        else: ok, index = recherchePremier(t,x,index+1)

    return ok, index

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
