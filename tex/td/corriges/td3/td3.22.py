# -*- coding: utf-8 -*-
 
def decodeIeee754(code):
    """
    x = decodeIeee754(code)
    valeur décimale du réel correspondant au code IEEE 754

    >>> decodeIeee754(ieee754(-31.7,2)[1])
    -31.7
    >>> decodeIeee754(ieee754(-31.7e-5,2)[1])
    -0.000317
    >>> decodeIeee754(ieee754(-31.7e5,2)[1])
    -3170000.0
    """
    assert type(code) is list
    assert len(code) == 32 or len(code) == 64

    ke, km, kieee, biais = precision754(len(code)//32)

    signe = (-1)**code[0]

    cexposant = code[1:ke+1]
    cmantisse = code[ke+1:km+ke+1]
    
    exposant = decodage(cexposant,2) - biais
    
    mantisse = 1
    for i in range(len(cmantisse)) :
        mantisse = mantisse + cmantisse[i]*2**(-i-1)
    
    x = signe*mantisse*2**exposant
    
    return x

#-----------------------------------------------------------------------
def ieee754(x,precision=1) :
    """
    (statut, code) = ieee754(x,precision)
    codage selon la norme IEEE 754 du réel x en simple précision
    (precision == 1) ou en double précision (precision == 2).
    Si statut == 'normal', code est le code IEEE754 recherché
    sinon statut = 'underflow' ou 'overflow' et code = [0]

    >>> ieee754(0.0,1)
    ('normal', [0,\
 0, 0, 0, 0, 0, 0, 0, 0,\
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    >>> ieee754(-0.0625,1)
    ('normal', [1,\
 0, 1, 1, 1, 1, 0, 1, 1,\
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    >>> ieee754(-0.0625e-250,1)
    ('underflow', [1,\
 0, 0, 0, 0, 0, 0, 0, 0,\
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    >>> ieee754(-0.0625e250,1)
    ('overflow', [1,\
 1, 1, 1, 1, 1, 1, 1, 1,\
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    >>> ieee754(0.0625,2)
    ('normal', [0,\
 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1,\
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    >>> ieee754(-0.0625e-250,2)
    ('normal', [1,\
 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0,\
 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1,\
 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0])
     >>> ieee754(173.2679,1)
     ('normal', [0,\
 1, 0, 0, 0, 0, 1, 1, 0,\
 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1])
     >>> ieee754(173.2679,2)
     ('normal', [0,\
 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0,\
 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0,\
 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0])
    """
    assert type(x) is float
    assert precision in [1,2]

    ke, km, kieee, biais = precision754(precision)

    statut = 'normal'
    code = [0 for i in range(kieee)]
    if x != 0.0 :
        statut, mantisse, exposant = mantisse_exposant(x,precision)
        code[0]            = signe(x)
        code[1:ke+2]       = exposant
        code[ke+1:km+ke+1] = mantisse

    return statut, code

#-----------------------------------------------------------------------
def precision754(precision) :
    assert precision in [1,2]
    
    if precision == 1 :
        ke, km, kieee, bias = 8, 23, 32, 127
    else :
        ke, km, kieee, bias = 11, 52, 64, 1023

    return ke, km, kieee, bias

#-----------------------------------------------------------------------
def mantisse_exposant(x,precision=1) :
    assert type(x) is float
    assert precision in [1,2]

    ke, km, kieee, bias = precision754(precision)
    cbias = codage(bias,2,ke,True)[1]
    
    pe, pf = partieEntiere(x), partieFractionnaire(x)
    
    expo, debut = 0, False
    statut, mantisse = codage(pe,2,km+1)

    if statut == 'overflow' :
        exposant = codage(2**ke-1,2,ke,True)[1]
        mantisse = codage(0,2,km,True)[1]
    else :
        if mantisse == [0] :
            debut = True
            mantisse = []

        expo = len(mantisse)-1  
        i = len(mantisse)
        while (pf != 0) and (i < km+1):
            pf = pf * 2
            pe = int(pf)
            pf = pf - pe
            if (pe == 0) and debut == True :
                expo = expo - 1
            else:
                debut = False
                mantisse.append(pe)
                i = i + 1
            
        if len(mantisse) > 0 and mantisse[0] == 1 :
            del mantisse[0]

        for i in range(len(mantisse),km):
            mantisse.append(0)

        if   expo >  bias  :
            statut = 'overflow'
            expo = 2**ke-1
            mantisse = codage(0,2,km,True)[1]
        elif expo <= -bias :
            statut = 'underflow'
            expo = -bias
            mantisse = codage(0,2,km,True)[1]
        else               :
            statut = 'normal'

        expo = expo + bias
        exposant = codage(expo,2,ke,True)[1]
        
    return statut, mantisse, exposant

#-----------------------------------------------------------------------
def signe(x) :
    """
    s = signe(x)
    signe du réel x, 0 si x > 0, 1 si x < 0
    >>> signe(5.7)
    0
    >>> signe(-5.7)
    1
    """
    assert type(x) is float
    
    return int(x < 0)

#-----------------------------------------------------------------------
def partieEntiere(x) :
    """
    pe = partieEntiere(x)
    partie entière du réel x

    >>> partieEntiere(0.67)
    0
    >>> partieEntiere(-0.67)
    0
    >>> partieEntiere(34.8)
    34
    """
    assert type(x) is float
    
    return int(abs(x))

#-----------------------------------------------------------------------
def partieFractionnaire(x) :
    """
    pf = partieFractionnaire(x)
    partie fractionnaire du réel x

    >>> partieFractionnaire(8.5)
    0.5
    >>> partieFractionnaire(-8.5)
    0.5
    >>> partieFractionnaire(0.5)
    0.5
    """
    assert type(x) is float
    
    return abs(x) - partieEntiere(x)

#-----------------------------------------------------------------------
def codage(n,b,k,remplir=False) :
    """
    statut, code = codage(n,b,k,remplir)
    code en base b sur k bits maximum l'entier décimal n
    statut = 'normal' si 0 <= n < b**k, 'overflow' sinon
    si remplir == True, on remplit à gauche de 0 pour avoir len(code) = k

    >>> codage(0,2,8,False)
    ('normal', [0])
    >>> codage(0,2,8,True)
    ('normal', [0, 0, 0, 0, 0, 0, 0, 0])
    >>> codage(256,2,8,False)
    ('overflow', [0])
    >>> codage(65,2,8,False)
    ('normal', [1, 0, 0, 0, 0, 0, 1])
    >>> codage(65,2,8,True)
    ('normal', [0, 1, 0, 0, 0, 0, 0, 1])
    >>> codage(65,5,4,True)
    ('normal', [0, 2, 3, 0])
    >>> codage(79,16,4,True)
    ('normal', [0, 0, 4, 15])
    """
    assert type(n) is int and n >= 0
    assert type(b) is int and b > 1
    assert type(k) is int and k > 0

    if n == 0 :
        statut = 'normal'
        code = [0]
    elif n >= b**k :
        statut = 'overflow'
        code = [0]
    else :
        statut = 'normal'
        code = []
        i = 0
        while (n != 0) and (i < k) :
                code.insert(0,n%b)
                n = n//b
                i = i + 1
                
    if remplir == True :
        diffLen = k - len(code)
        for i in range(diffLen):
            code.insert(0,0)
    
    return statut, code

#-----------------------------------------------------------------------
def decodage(code,b=2) :
    """
    n = decodage(code,b)
    valeur décimale de l'entier correspondant au code en base b
    
    >>> decodage(codage(0,2,8,False)[1],2)
    0
    >>> decodage(codage(65,2,8,True)[1],2)
    65
    >>> decodage(codage(79,16,4,True)[1],16)
    79
    """
    assert type(code) is list
    assert type(b) is int and b > 1

    x = 0
    for i in range(len(code)) :
        c = code[len(code)-1-i]
        x = x + c*b**i

    return x

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
