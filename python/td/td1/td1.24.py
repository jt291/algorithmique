# -*- coding: utf-8 -*-
 
# avec la tortue Logo
from turtle import *

# Pentagone régulier de 10 pas de côté
# avance de 10 pas
forward(10)
# tourne à gauche de (360/5)°
left(360/5)
# avance de 10 pas
forward(10)
# tourne à gauche de (360/5)°
left(360/5)
# avance de 10 pas
forward(10)
# tourne à gauche de (360/5)°
left(360/5)
# avance de 10 pas
forward(10)
# tourne à gauche de (360/5)°
left(360/5)
# avance de 10 pas
forward(10)
# tourne à gauche de (360/5)°
left(360/5)

# Pentagone régulier de 10 pas de côté
# répète 5 fois de suite
for i in [1,2,3,4,5] :
#  les 2 instructions
# avance de 10 pas,
    forward(10)
# tourne à gauche de (360/8)°
    left(360/5)

# Hexagone régulier de 10 pas de côté
# répète 6 fois de suite
for i in [1,2,3,4,5,6] :
#  les 2 instructions
# avance de 10 pas,
    forward(10)
# tourne à gauche de (360/8)°
    left(360/6)

# Octogone régulier de 10 pas de côté
# répète 8 fois de suite
for i in [1,2,3,4,5,6,7,8] :
#  les 2 instructions
# avance de 10 pas,
    forward(10)
# tourne à gauche de (360/8)°
    left(360/8)

# Polygone régulier de n côtés de 10 pas chacun
# répète n fois de suite (par exemple n = 113)
n = 113
for i in range(n) :
#  les 2 instructions
# avance de 10 pas,
    forward(10)
# tourne à gauche de (360/8)°
    left(360/n)
