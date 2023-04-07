# -*- coding: utf-8 -*-
 
n = 83
b = 8
k = 8

code = []
quotient = n
for i in range(k): code.append(0)
    
i = k - 1
while quotient != 0 and i >= 0:
    code[i] = quotient%b
    quotient = quotient//b
    i = i - 1

print(n,b,k,'->',code)
