# -*- coding: utf-8 -*-
 
# assurance à points
age = 23
anciennete = 3
fidelite = 1
n = 0

pts = 0
if age < 25        : pts = pts + 1          # jeune
if anciennete < 2  : pts = pts + 1          # jeune conducteur
pts = pts + n                               # accidents
if pts < 3 and fidelite > 1 : pts = pts - 1 # fidélité
if   pts == -1 : print('tarif A')
elif pts == 0  : print('tarif B')
elif pts == 1  : print('tarif C')
elif pts == 2  : print('tarif D')
else           : print('refus d\'assurer') 
