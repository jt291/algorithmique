# -*- coding: utf-8 -*-
 
def inverser(s):
    """
    sinv = inverser(s)
    chaîne dont les caractères sont dans l'ordre inverse de la chaîne s

    >>> inverser('inverser')
    'resrevni'
    >>> inverser('kayak')
    'kayak'
    >>> inverser('')
    ''
    """
    assert type(s) is str

    sinv = ''
    for c in s:
        sinv = c + sinv

    return sinv

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
