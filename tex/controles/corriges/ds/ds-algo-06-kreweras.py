# -*- coding: utf-8 -*-
 
def g(n,m):
    assert type(n) is int
    assert type(m) is int
    assert 0 <= m and m <= n
    if n == 0 and m == 0:
        c = 1
    else:
        if m == 0: c = 0
        else:
            c = 0
            for i in range(1,m+1):
                c = c + g(n-1,n-i)
    return c


#-----------------------------------------------------------------------
for n in range(7):
    print(n,':',end=' ')
    for m in range(n+1):
        print(g(n,m),end=' ')
    print()

#-----------------------------------------------------------------------
from math import pi, fabs
print(fabs(pi-12*g(5,5)/g(6,6))/pi < 0.01)
