# -*- coding: utf-8 -*-
 
# swap : version 1
x, y = 1, 2
print('1 avant :',x,y)

tmp = x
x = y
y = tmp
print('1 après :',x,y,' il y a permutation des originaux')

# swap : version 2
def swap(x,y):
    tmp = x
    x = y
    y = tmp
    print('2 pendant :',x,y,' il y a bien permutation des copies')
    return

x, y = 1, 2
print('2 avant   :',x,y)

swap(x,y)
print('2 après   :',x,y,' mais pas des originaux')
