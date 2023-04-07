# -*- coding: utf-8 -*-
 
ga  = 0
bu  = 1
zo  = 2
meu = 3

#-----------------------------------------------------------------------
def corrige(a,b):
    assert type(a) is list
    assert type(b) is list

    ca = decodage(a,4)
    cb = decodage(b,4)
    q = codage(ca//cb,4)
    r = codage(ca%cb,4)

    printShadok(a)
    print('÷ ',end=' ')
    printShadok(b)
    print('\t-> quotient = ',end=' ')
    printShadok(q)
    print(', reste = ',end=' ')
    printShadok(r)
    print()
    
    return q,r
    
#-----------------------------------------------------------------------
def decodage(code,b) :
    assert type(code) is list
    n = 0
    for i in range(len(code)) :
        n = n + code[len(code)-1-i]*b**i
    return n

#-----------------------------------------------------------------------
def codage(n,b) :
    assert type(n) is int and n >= 0
    assert type(b) is int and b > 1

    if n == 0 : code = [0]
    else :
        code = []
        while n > 0 :
            r = n%b
            n = n//b
            code.insert(0,r)

    return code

#-----------------------------------------------------------------------
def printShadok(code) :
    assert type(code) is list

    for e in code:
        if e == 0   : ce = 'ga'
        elif e == 1 : ce = 'bu'
        elif e == 2 : ce = 'zo'
        elif e == 3 : ce = 'meu'
        else        : ce = 'problème'
        print(ce,end=' ')
    return

#-----------------------------------------------------------------------
# 1.
a, b = [meu, zo, bu, meu], [zo, zo, zo]
corrige(a,b)

# 2.
a, b = [zo, meu, ga, zo], [bu, meu, zo]
corrige(a,b)

# 3.
a, b = [bu, ga, zo, meu], [meu, zo, zo]
corrige(a,b)

# 4.
a, b = [meu, zo, ga, bu], [meu, zo, zo]
corrige(a,b)

# 5.
a, b = [bu, zo, bu, zo], [bu, ga, zo]
corrige(a,b)

# 6.
a, b = [bu, ga, meu, bu], [bu, ga, ga]
corrige(a,b)

# 7.
a, b = [zo, bu, zo, meu], [zo, ga, bu]
corrige(a,b)

# 8.
a, b = [meu, zo, ga, bu], [zo, bu, ga]
corrige(a,b)

# 9.
a, b = [bu, meu, meu, ga], [bu, meu, ga]
corrige(a,b)

# 10.
a, b = [zo, bu, meu, meu], [bu, ga, bu]
corrige(a,b)

# 11.
a, b = [zo, ga, zo, meu], [zo, ga, zo]
corrige(a,b)

# 12.
a, b = [bu, meu, bu, ga], [meu, zo, meu]
corrige(a,b)

# 13.
a, b = [zo, meu, bu, zo], [bu, ga, meu]
corrige(a,b)

# 14.
a, b = [zo, ga, meu, meu], [bu, zo, ga]
corrige(a,b)

# 15.
a, b = [meu, meu, ga, zo], [zo, meu, meu]
corrige(a,b)

# 16.
a, b = [bu, ga, zo, meu], [bu, ga, zo]
corrige(a,b)

# 17.
a, b = [zo, zo, ga, meu], [bu, ga, ga]
corrige(a,b)

# 18.
a, b = [zo, meu, meu, ga], [zo, meu, ga]
corrige(a,b)

# 19.
a, b = [zo, bu, bu, zo], [zo, bu, ga]
corrige(a,b)

# 20.
a, b = [meu, bu, bu, zo], [meu, bu, ga]
corrige(a,b)

# 21.
a, b = [meu, ga, zo, meu], [meu, ga, zo]
corrige(a,b)

# 22.
a, b = [bu, bu, zo, zo], [bu, ga, bu]
corrige(a,b)

# 23.
a, b = [bu, zo, ga, bu], [bu, zo, zo]
corrige(a,b)

# 24.
a, b = [meu, ga, meu, bu], [bu, meu, ga]
corrige(a,b)
