# -*- coding: utf-8 -*-
 
def cml(s):
    """
    (nc, nm, nl) = cml(s)
    nc est le nombre de caractères de la chaîne s,
    nm le nombre de mots et nl le nombre de lignes

    >>> s = "j'ai deux soeurs et 1 frère !"
    >>> cml(s)
    (29, 7, 1)
    >>> s = "j'ai deux soeurs\\n et 1 frère !"
    >>> cml(s)
    (30, 7, 2)
    >>> s = ''
    >>> cml(s)
    (0, 0, 0)
    """
    assert type(s) is str

    nc, nm, nl = 0, 0, 1
    if s == '' : nl = 0
    
    mot = False

    for c in s:
        if c.isalnum() :
            if not mot:
                nm = nm + 1
                mot = True
        elif c.isspace() :
            if c == '\n' : nl = nl + 1
            mot = False
        else:
            mot = False
        nc = nc + 1
    assert nc == len(s) # vérification
    
    return nc, nm, nl

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
