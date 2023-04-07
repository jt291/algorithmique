# -*- coding: utf-8 -*-
 
def hanoi(n,a,b,c):
    """
    déplace n disques de la tour a à la tour c
    en utilisant la tour b

    >>> hanoi(1,'a','b','c')
    disque 1 de a vers c
    >>> hanoi(2,'a','b','c')
    disque 1 de a vers b
    disque 2 de a vers c
    disque 1 de b vers c
    >>> hanoi(3,'a','b','c')
    disque 1 de a vers c
    disque 2 de a vers b
    disque 1 de c vers b
    disque 3 de a vers c
    disque 1 de b vers a
    disque 2 de b vers c
    disque 1 de a vers c
    >>> hanoi(4,'a','b','c')
    disque 1 de a vers b
    disque 2 de a vers c
    disque 1 de b vers c
    disque 3 de a vers b
    disque 1 de c vers a
    disque 2 de c vers b
    disque 1 de a vers b
    disque 4 de a vers c
    disque 1 de b vers c
    disque 2 de b vers a
    disque 1 de c vers a
    disque 3 de b vers c
    disque 1 de a vers b
    disque 2 de a vers c
    disque 1 de b vers c
    """
    assert type(n) is int and n >= 0

    if n > 0:
        hanoi(n-1,a,c,b)
        print('disque',n,'de',a,'vers',c)
        hanoi(n-1,b,a,c)
    else: pass
    return

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
