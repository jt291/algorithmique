# -*- coding: utf-8 -*-
 
# suite arithmétique 1 : version itérative
# n additions
n = 12573

i, somme = 0, 0
while i <= n :
    somme = somme + i
    i = i + 1
print('itérative :',n,'->',somme)

# suite arithmétique 2 : version constante
# 3 opérations
n = 12573

somme = n*(n+1)//2
print('constante :',n,'->',somme)
