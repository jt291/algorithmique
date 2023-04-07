# -*- coding: utf-8 -*-
 
from random import randint

# Génération de listes d'entiers.
def liste(n):
    assert type(n) is int and n >= 0
    t = []
    for i in range(n):
        t.append(randint(0,n))
    return t

# Génération de n-uplets d'entiers.
def nuplet(n):
    assert type(n) is int and n >= 0
    t = ()
    for i in range(n):
        t = t + (randint(0,n),)
    return t

# Génération de chaînes de caractères.
def chaine(n):
    assert type(n) is int and n >= 0
    t = ''
    for i in range(n):
        t = t + chr(randint(32,127))
    return t

# Exemples
for n in [0,5,10] :
    print(n,liste(n),nuplet(n),'"',chaine(n),'"')
