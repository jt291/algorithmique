# -*- coding: utf-8 -*-
 
# affectation
ht , r, tva = 12.35 , 3.5, 5.5
ttc = ht*(1-r /100)*(1+ tva /100)

print(ht < ttc < ht*(1+tva/100))

# tests
nt = 1000
n1 , n2 = 100 , 600
p1 , p2 , pm = 0.1, 0.08 , 0.05
if   nt < n1 : pt = nt*p1
elif nt < n2 : pt = n1*p1 + (nt -n1)*p2
else         : pt = n1*p1 + (n2 -n1 )*p2 + (nt -n2)*pm

print(nt,'->',pt)

# boucles
from math import *

f, a, b = cos, -pi/4, pi/4
n = 100
w = (b - a)/n
x = a + w/2
s = f(x)
while not (x > (b - w/2)):
    x = x + w
    s = s + f(x)
s = w*s

print(f,a,b,' -> ',s,sqrt(2))

# instructions imbriquées
from math import *

f, a, b = cos , 1, 2
s = 1.e-9
x1 , x2 = a, b
x = (x1 + x2 )/2
while not ((x2 - x1) <= s):
     if f(x1 )*f(x) < 0 : x2 = x
     else               : x1 = x
     x = (x1 + x2 )/2

print(f,a,b,' -> ',x,pi/2)

# exécution d'une séquence d'instructions
# triangle de Pascal
k = 6
n = 0
while n <= k:
    j = 0
    while j <= n:
        num , den = 1, 1
        i = 1
        while i <= j:
             num = num * (n - i + 1)
             den = den * i
             i = i + 1
        c = num // den
        print (c,end=' ')
        j = j + 1
    print ()
    n = n + 1
    

