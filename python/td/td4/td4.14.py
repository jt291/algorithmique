# -*- coding: utf-8 -*-
 
# la recherche dichotomique n'assure pas automatiquement
# de trouver la première occurence de la valeur recherchée

#-----------------------------------------------------------------------
def dichotomie(t,x,gauche,droite) :
    """
    ok,m = dichotomie(t,x,gauche,droite)
    recherche dichotomique de x dans une séquence t triée
    entre les indices gauche et droite
    ok == True si x a été trouvée à l'indice m,
    False sinon

    >>> t = [1,3,5,6,6,6,6,9]
    >>> dichotomie(t,6,0,len(t)-1)
    (True, 3)
    >>> t = [1,3,5,6,6,9]
    >>> dichotomie(t,6,0,len(t)-1)
    (True, 4)
    """
    assert type(t) is list
    assert 0 <= gauche <= droite < len(t)
    
    ok, m = False, (gauche + droite)//2
    if gauche > droite :
        ok = False
    else :
        if t[m] == x :
            ok = True
        elif t[m] > x :
            ok,m = dichotomie(t,x,gauche,m-1)
        else :
            ok,m = dichotomie(t,x,m+1,droite)

    return ok,m

#-----------------------------------------------------------------------
def dichotomie1(t,x,gauche,droite) :
    """
    ok,m = dichotomie1(t,x,gauche,droite)
    recherche dichotomique de la première occurence de x
    dans une séquence t triée
    entre les indices gauche et droite
    ok == True si x a été trouvée à l'indice m,
    False sinon

    >>> t = [1,3,5,6,6,6,6,9]
    >>> dichotomie1(t,6,0,len(t)-1)
    (True, 3)
    >>> t = [1,3,5,6,6,9]
    >>> dichotomie1(t,6,0,len(t)-1)
    (True, 3)
    >>> dichotomie(t,6,0,len(t)-1) == dichotomie1(t,6,0,len(t)-1)
    False
    """
    assert type(t) is list
    assert 0 <= gauche <= droite < len(t)
    
    ok, m = False, (gauche + droite)//2
    if gauche > droite :
        ok = False
    else :
        if t[m] == x :
            ok = True
            m1 = m
            # recherche de la 1ère occurence
            while t[m1] == x and m1 >= 0 :
                m1 = m1 - 1
                if t[m1] == x : m = m1;
        elif t[m] > x :
            ok,m = dichotomie1(t,x,gauche,m-1)
        else :
            ok,m = dichotomie1(t,x,m+1,droite)

    return ok,m

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
