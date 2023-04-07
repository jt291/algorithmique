# -*- coding: utf-8 -*-
 
def application(f,t):
    """
    t = application(f,t)
    applique la fonction f à chaque élément de la liste t

    >>> s = [-1,0,-4,3,5,-7]
    >>> application(abs,s)
    [1, 0, 4, 3, 5, 7]
    >>> s = [0,1,2,3]
    >>> f = lambda x: x+2
    >>> application(f,s)
    [2, 3, 4, 5]
    """
    assert type(t) is list
    
    for i in range(len(t)):
        t[i] = f(t[i])
        
    return t

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
