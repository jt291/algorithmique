# -*- coding: utf-8 -*-
 
def neg2(code):
    """
    neg = neg2(code)
    complément à 2 d'un entier binaire

    >>> neg2([0,0,0,1,0,1,1,1])
    [1, 1, 1, 0, 1, 0, 0, 1]
    >>> neg2([1, 1, 1, 0, 1, 0, 0, 1])
    [0, 0, 0, 1, 0, 1, 1, 1]

    >>> for a in [0,1]:
    ...    for b in [0,1]:
    ...        for c in [0,1]:
    ...            add2([a,b,c],neg2([a,b,c]))
    [0, 0, 0]
    [1, 0, 0, 0]
    [1, 0, 0, 0]
    [1, 0, 0, 0]
    [1, 0, 0, 0]
    [1, 0, 0, 0]
    [1, 0, 0, 0]
    [1, 0, 0, 0]
    """

    assert type(code) is list
    neg = []

    carry = 1
    for i in range(len(code)): neg.append(int(not code[i]))
    for i in range(len(code)):
        value = neg[len(code)-1-i] + carry
        if value >= 2:
            neg[len(code)-1-i] = value - 2
            carry = 1
        else:
            neg[len(code)-1-i] = value
            carry = 0

    return neg

#-----------------------------------------------------------------------
def add2(code1,code2):
    """
    sum2 = add2(code1,code2)
    addition binaire code1 + code2

    >>> add2([1,0,1],[1])
    [1, 1, 0]
    >>> add2([1,0,1],[1,0])
    [1, 1, 1]
    >>> add2([1,0],[1,0,1])
    [1, 1, 1]
    >>> add2([1,0,1],[1,1])
    [1, 0, 0, 0]
    """
    assert type(code1) is list
    assert type(code2) is list

    sum2 = []
    diffLen = len(code1) - len(code2)
    if diffLen > 0:
        for i in range(diffLen): code2.insert(0,0)
    else:
        for i in range(-diffLen): code1.insert(0,0)

    for i in range(len(code1)): sum2.append(0)

    carry = 0
    for i in range(len(code1)-1,-1,-1):
        value = code1[i] + code2[i] + carry
        if value >= 2:
            sum2[i] = value - 2
            carry = 1
        else:
            sum2[i] = value
            carry = 0

    if carry == 1: sum2.insert(0,1)

    return sum2

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
