# -*- coding: utf-8 -*-
 
# recherche dans un annuaire

#-----------------------------------------------------------------------
def annuaire(a) :
    """
    ok = annuaire(a)
    True si a est un annuaire : une liste de paires (nom,numéro)

    >>> annuaire([])
    True
    >>> annuaire([('jean','0607080910'),('paul','0298000102')])
    True
    >>> annuaire([1,2,4])
    False
    """
    ok = False
    if type(a) is list :
        i = 0
        ok = True
        while i < len(a) and ok :
            if type(a[i]) is not tuple or len(a[i]) != 2 :
                ok = False
            else :
                i = i + 1

    return ok

#-----------------------------------------------------------------------
def numero(nom,a) :
    """
    num = numero(nom,a)
    numero correspondant au nom dans l'annuaire a

    >>> annuaire = [('jean','0607080910'),('paul','0298000102')]
    >>> numero('paul',annuaire)
    '0298000102'
    >>> numero('pierre',annuaire)
    ''
    """
    assert annuaire(a)

    num, i = '', 0
    while i < len(a) and num == '' :
        if a[i][0] == nom :
            num = a[i][1]
        else:
            i = i + 1

    return num

#-----------------------------------------------------------------------
def nom(numero,a) :
    """
    n = nom(numero,a)
    nom correspondant au numero dans l'annuaire a

    >>> annuaire = [('jean','0607080910'),('paul','0298000102')]
    >>> nom('0298000102',annuaire)
    'paul'
    >>> nom('0298000000',annuaire)
    ''
    >>> nom(numero('paul',annuaire),annuaire) == 'paul'
    True
    """
    assert annuaire(a)

    n, i = '', 0
    while i < len(a) and n == '' :
        if a[i][1] == numero :
            n = a[i][0]
        else :
            i = i + 1

    return n

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
