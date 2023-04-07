# -*- coding: utf-8 -*-
 
# itérations 1
print('--- itérations 1:')
x = 0
while x != 33:
    x = int(input('entrer un nombre : '))

# itérations 2
print('--- itérations 2:')
x = 0
while x <= 0 or x > 5 :
    x = int(input('entrer un nombre : '))

# itérations 3
print('--- itérations 3: somme de 5 nombres')
s = 0
for i in range(5) :
    x = int(input('entrer un nombre : '))
    s = s + x
print(s)

# itérations 4
print('--- itérations 4:  triangle d\'étoiles')
for i in range(0,10) :
    for j in range(0,i) :
        print('*',end=' ')
    print()

# itérations 5
print('--- itérations 5: triangle d\'étoiles inversé')
for i in range(0,10) :
    j = 10 - i
    while j > 0 :
        print('*',end=' ')
        j = j - 1
    print()

# itérations 6
print('--- itérations 6: tables de multiplication')
for i in range(1,10):
    for j in range(0,11) :
        print(i, 'x', j, ' = ', i*j)
    print()

# itérations 7
print('--- itérations 7: triangle de Pascal')
for n in range(10) :
    for p in range(n+1) :
        num = 1
        den = 1
        for i in range(1,p+1) :
            num = num*(n-i+1)
            den = den*i
        c = num//den
        print(c,end=' ')
    print()

# itérations 8
print('--- itérations 8: nombres de Fibonacci')
for n in range(0,15) :
    f, f1, f2 = 1, 1, 1
    for i in range(2,n+1) :
        f = f1 + f2
        f2 = f1
        f1 = f
    print(f,end=' ')
print()

# itérations 9
print('--- itérations 9: codage binaire')
b = 2
k = 8
n = 23
s = 0
i = k - 1
q = n
while q != 0 and i >= 0 :
    s = s + (q%b)*b**(k-1-i)
    print(q%b,end=' ')
    q = q//b
    i = i - 1
