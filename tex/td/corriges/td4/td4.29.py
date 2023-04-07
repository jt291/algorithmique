# -*- coding: utf-8 -*-
 
from td425 import matriceCarree
from math import fabs

#-----------------------------------------------------------------------
def solve(a,b):
    """
    x = solve(a,b)
    x est la solution de l'équation matricielle a*x = b
    
    >>> a, b = [[4]], [1]
    >>> solve(a,b)
    [0.25]
    >>> a, b = [[1,1],[1,-1]], [1,0]
    >>> solve(a,b)
    [0.5, 0.5]
    >>> a = [[2,-1,2],[1,10,-3],[-1,2,1]]
    >>> b = [2,5,-3]
    >>> solve(a,b)
    [2.0, 0.0, -1.0]
    """
    assert matriceCarree(a) 
    assert type(b) is list
    assert len(a) == len(b)
    
    if triangularisation(a,b) == True:
        x = backsubstitutions(a,b)
    else: x = []
    
    return x

#-----------------------------------------------------------------------
def pivot(a,i0):
    maxi = fabs(a[i0][i0])
    r = i0
    for i in range(i0+1,len(a)):
      if fabs(a[i][i0]) > maxi:
          maxi = fabs(a[i][i0])
          r = i
    return r

#-----------------------------------------------------------------------
def substractRows(a,b,k,i):
    q = 1.*a[k][i]/a[i][i]
    a[k][i] = 0
    b[k] = b[k] - q*b[i]
    for j in range(i+1,len(a)):
        a[k][j] = a[k][j] - q*a[i][j]
    return 

#-----------------------------------------------------------------------
def triangularisation(a,b):
   ok = True; i = 0
   while i < len(a) and ok == True:
      p = pivot(a,i)
      if i != p:
         a[i],a[p] = a[p],a[i]
         b[i],b[p] = b[p],b[i]
      if a[i][i] == 0: ok = False
      else:
         for k in range(i+1,len(a)):
            substractRows(a,b,k,i)
      i = i + 1
   return ok

#-----------------------------------------------------------------------
def backsubstitutions(a,b):
    n = len(a); x = []
    for k in range(n): x.append(0)
    
    x[n-1] = 1.*b[n-1]/a[n-1][n-1]
    for i in range(n-2,-1,-1): 
        x[i] = b[i]
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]
        x[i] = 1.*x[i]/a[i][i]
    return x

#-----------------------------------------------------------------------
a = [[ 1,  0, 0, -1,  1, 0],\
     [ 1,  1, 0,  0,  0,-1],\
     [ 0,  1,-1,  0, -1, 0],\
     [10,-10, 0,  0,-10, 0],\
     [ 0,  0, 5,-20,-10, 0],\
     [ 0, 10, 5,  0,  0,10]]
b = [0,0,0,0,0,12]
print(a,b)
print(solve(a,b))
print()

a, b = [[10,7,8,7],[7,5,6,5],[8,6,10,9],[7,5,9,10]], [32,23,33,31]
print(a,b)
print(solve(a,b))
print()

a, b = [[10,7,8.1,7.2],[7.08,5.04,6,5],[8,5.98,9.89,9],[6.99,4.99,9,9.98]], [32,23,33,31]
print(a,b)
print(solve(a,b))
print()

a, b = [[10,7,8,7],[7,5,6,5],[8,6,10,9],[7,5,9,10]], [32.01,22.99,33.01,30.99]
print(a,b)
print(solve(a,b))
print()


#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
