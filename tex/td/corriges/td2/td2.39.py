# -*- coding: utf-8 -*-
 
n = 20
if   n > 30 : prix = 10*0.1 + 20*0.09 + (n - 30)*0.08
elif n > 10 : prix = 10*0.1 + (n - 10)*0.09
else        : prix = n*0.1
print(n,'->',prix)
