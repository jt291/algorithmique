# -*- coding: utf-8 -*-
 
# somme arithmétique : version constante
a, b, n = 0, 1, 5
s = a*(n+1) + b*n*(n+1)//2
print('somme arithmétique :',a,b,n,'->',s)

# somme arithmétique : version itérative
a, b, n = 0, 1, 5
s = 0
for i in range(n+1):
    s = s + a + b*i
print('somme arithmétique :',a,b,n,'->',s)

# somme géométrique : version constante
a, b, n = 1, 2, 5
s = a*(b**(n+1) - 1)//(b-1)
print('somme géométrique  :',a,b,n,'->',s)

# somme géométrique : version itérative
a, b, n = 1, 2, 5
s = 0
for i in range(n+1):
    s = s + a*b**i
print('somme géométrique  :',a,b,n,'->',s)
