# -*- coding: utf-8 -*-
 
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
