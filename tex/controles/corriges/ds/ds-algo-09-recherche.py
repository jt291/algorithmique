# -*- coding: utf-8 -*-
 
def recherchekieme(t,x,k):
    """
    ok,i = recherchekieme(t,x,k)
    recherche la kième occurence de x dans la liste t en commençant
    par la fin de la liste.
    ok == True si x a été trouvé à l'indice i, False sinon

    >>> recherchekieme([1,2,1,3,4,1,5],1,2)
    (True, 2)
    >>> recherchekieme([1,2,1,3,4,1,5],1,4)
    (False, -1)
    """
    assert type(t) is list
    assert type(k) is int and k > 0

    ok, i = False, len(t) - 1
    occur = 0
    while i >= 0 and not ok:
            if t[i] == x:
                occur = occur + 1
                if occur == k: ok = True
                else: i = i - 1
            else: i = i - 1

    return ok, i

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
