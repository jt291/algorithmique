# -*- coding: utf-8 -*-
 
# Matrice
def matrice(t):
    """
    ok = matrice(t)
    True si t est une matrice, False sinon
    
    >>> matrice(5)
    False
    >>> matrice([])
    False
    >>> matrice([5])
    False
    >>> matrice([[5]])
    True
    >>> matrice([[5,6],[7]])
    False
    >>> matrice([[5,6,7],[8,9]])
    False
    >>> matrice([[5,6,7],[8,9,3]])
    True
    """
    ok = True
    if type(t) is not list or t == []:
        ok = False
    elif type(t[0]) is not list: 
        ok = False
    else:
        i, n, m = 1, len(t), len(t[0])
        while i < n and ok == True:
            if type(t[i]) is not list:
                ok = False
            elif len(t[i]) != m: 
                ok = False
            i = i + 1
            
    return ok

# Matrice carrée
def matriceCarree(t):
    """
    ok = matriceCarree(t)
    True si t est une matrice carrée, False sinon
    
    >>> matriceCarree([[4,5,6],[7,8,9]])
    False
    >>> matriceCarree([[5,6],[8,9]])
    True
    >>> matriceCarree([[]])
    False
    """
    assert matrice(t)
    
    if len(t) > 0 and len(t[0]) == len(t):
        ok = True
    else: ok = False
    
    return ok

# Matrice symétrique
def matriceSymetrique(t):
    """
    ok = matriceSymetrique(t)
    True si t est une matrice carrée symétrique, False sinon
    
    >>> matriceSymetrique([[5,6],[8,9]])
    False
    >>> matriceSymetrique([[5,6],[6,9]])
    True
    >>> matriceSymetrique([[5,6,7],[6,8,9],[7,9,3]])
    True
    """
    assert matriceCarree(t)
    
    ok,i = True,0
    while i < len(t) and ok == True:
        j = i + 1
        while j < len(t[0]) and ok == True:
            if t[i][j] != t[j][i]: 
                ok = False
            else: j = j + 1
        i = i + 1
        
    return ok

# Matrice diagonale
def matriceDiagonale(t):
    """
    ok = matriceDiagonale(t)
    True si t est une matrice carrée diagonale, False sinon
    
    >>> matriceDiagonale([[5,6],[8,9]])
    False
    >>> matriceDiagonale([[5,0],[0,9]])
    True
    >>> matriceDiagonale([[5,0,0],[0,0,0],[0,0,3]])
    True
    """
    assert matriceCarree(t)
    
    ok,i = True,0
    while i < len(t) and ok == True:
        j = 0
        while j < len(t[0]) and ok == True:
            if i != j and t[i][j] != 0:
                ok = False
            else: j = j + 1
        i = i + 1
        
    return ok

# Multiplication d'une matrice par un scalaire
def multiplicationScalaire(t,x):
    """
    multiplicationScalaire(t,x)
    multiplie la matrice t par le nombre x
    
    >>> multiplicationScalaire([[5,6],[2,7]],3)
    [[15, 18], [6, 21]]
    """
    assert matrice(t)
    assert type(x) is int or type(x) is float
    
    for i in range(len(t)):
        for j in range(len(t[0])):
            t[i][j] = x*t[i][j]
            
    return t

# Transposée d'une matrice
def transposee(t):
    """
    s = transposee(t)
    matrice transposée de la matrice t
    
    >>> transposee([[1,2],[4,5]])
    [[1, 4], [2, 5]]
    >>> transposee([[1,2,3],[4,5,6]])
    [[1, 4], [2, 5], [3, 6]]
    """
    assert matrice(t)
    
    s = []
    for j in range(len(t[0])):
        s.append([])
        for i in range(len(t)):
            s[j].append(t[i][j])
            
    return s

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
