# -*- coding: utf-8 -*-
 
x = 140.8125

# signe
s = int(x < 0)
cs = [s]
print('signe :',x,s,cs)

# partie entière
pe = int(abs(x))

b = 2
cpe = []
quotient = pe
while quotient != 0:
    cpe.insert(0,quotient%b)
    quotient = quotient//b
print('partie entière :',x,pe,cpe)

# partie fractionnaire
pf = abs(x) - pe

b = 2
cpf = []
fraction = pf
while fraction != 0:
    cpf.append(int(fraction*b))
    fraction = fraction*b - int(fraction*b)
print('partie fractionnaire :',x,pf,cpf)

# mantisse
mantisse = cpe + cpf
print('mantisse :',x,mantisse)

# exposant
exposant = len(cpe)-1

b = 2
cexposant = []
quotient = exposant
while quotient != 0:
    cexposant.insert(0,quotient%b)
    quotient = quotient//b
print('exposant :',x,exposant,cexposant)

# affichage
print(x,' -> ','(-1)**',s,sep='',end='')
print('*(',mantisse[0],'.',sep='',end='')
for i in range(1,len(mantisse)): print(mantisse[i],sep='',end='')
print(')*',b,'**(',sep='',end='')
for i in range(0,len(cexposant)): print(cexposant[i],sep='',end='')
print(')')
