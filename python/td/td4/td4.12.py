# -*- coding: utf-8 -*-
 

#-----------------------------------------------------------------------
def matrice(a):
    """
    ok = matrice(a)
    teste si a est une matrice

    >>> matrice([[1,2],[3,4],[5,6]])
    True
    >>> matrice([[1,2],[3,4],[5,6,7]])
    False
    >>> matrice([])
    False
    >>> matrice([[],[],[]])
    False
    """
    ok = False
    if type(a) is list and len(a) != 0 and\
       type(a[0]) is list and len(a[0]) != 0 :
        ok = True
        arow = len(a)
        acol = len(a[0])

        i = 1
        while i < len(a) and ok :
            if type(a[i]) is not list or len(a[i]) != len(a[0]) :
                ok = False
            else :
                i = i + 1

    return ok

#-----------------------------------------------------------------------
def nrow(a) :
    """
    n = nrow(a)
    nombre de lignes de la matrice a

    >>> nrow([[1,2],[3,4],[5,6]])
    3
    >>> nrow([[1,2,3,4]])
    1
    """ 
    assert matrice(a)
    
    return len(a)

#-----------------------------------------------------------------------
def ncol(a) :
    """
    n = ncol(a)
    nombre de colonnes de la matrice a

    >>> ncol([[1,2],[3,4],[5,6]])
    2
    >>> ncol([[1,2,3,4]])
    4
    """ 
    assert matrice(a)
    
    return len(a[0])

#-----------------------------------------------------------------------
def multMatrice(a,b):
    """
    c = multMatrice(a,b)
    produit matriciel des matrices a et b

    >>> a = [[1,1,1],[2,4,8],[3,9,27]]
    >>> b = [[-1],[1],[1]]
    >>> multMatrice(a,b)
    [[1], [10], [33]]
    >>> a = [[2,-1,2],[1,10,-3],[-1,2,1]]
    >>> b = [[2],[0],[-1]]
    >>> multMatrice(a,b)
    [[2], [5], [-3]]
    >>> a = [[1,1],[2,2],[3,3]]
    >>> b = [[-1,-1,-1],[-2,-2,-2]]
    >>> multMatrice(a,b)
    [[-3, -3, -3], [-6, -6, -6], [-9, -9, -9]]
    >>> a = [[2]]
    >>> b = [[1,2,3,4,5]]
    >>> multMatrice(a,b)
    [[2, 4, 6, 8, 10]]
    """
    assert matrice(a) and matrice(b)
    assert ncol(a) == nrow(b)

    arow, acol = nrow(a), ncol(a)
    brow, bcol = nrow(b), ncol(b)
    
    c = []
    for i in range(arow) :
        c.append([])
        for j in range(bcol) :
            c[i].append(0)
        
    for i in range(arow) :
        for j in range(bcol) :
            for k in range(acol) :
                c[i][j] = c[i][j] + a[i][k]*b[k][j]

    return c

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
