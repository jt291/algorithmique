# -*- coding: utf-8 -*-
 
x = 0.2578125
k = 60
print(x,'= 0.',end=' ')
while x != 0 and k > 0:
    x = x*2
    print(int(x),end=' ')
    x = x - int(x)
    k = k - 1
