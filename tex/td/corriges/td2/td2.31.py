# -*- coding: utf-8 -*-
 
x = -1
if x < 0: x = 3
else: x = -x
print('alternative simple :',x)

x = -1
if x < 0: x = 3
if not x < 0: x = -x
print('2 tests simples :',x)
