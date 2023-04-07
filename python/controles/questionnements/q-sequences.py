# -*- coding: utf-8 -*-
 
item1 = ('dupont', 23, 'brest', '06789656')
item2 = ('abgral', 61, 'lille', '06231298')
item3 = ('dupont', 23, 'brest', '02989656')
item4 = ('abgral', 67, 'brest', '06556438')
item5 = ('martin', 38, 'paris', '01674523')
item6 = ('abgral', 67, 'lille', '06231298')

annuaire    = [item1, item2, item3, item4, item5, item6]
croissant   = lambda x,y : x < y
decroissant = lambda x,y : x > y

#-----------------------------------------------------------------------
def triAnnuaire(annuaire,cles,ordre) :
    assert type(cles) is list and len(cles) == 4
    assert ordre == croissant or ordre == decroissant
    
    cmp = lambda x,y : cmpItems(x,y,cles,ordre)
    triInsertion(annuaire,cmp)
    return

    
#-----------------------------------------------------------------------
def triInsertion (t,cmp =( lambda x,y : x < y)) :
    assert type(t) is list
    for i in range (1, len(t)):
        x = t[i]
        k = i
        for j in range(i -1, -1 , -1):
            if not cmp(t[j],x) :
                 k = k-1
                 t[j+1] = t[j]
        t[k] = x
    return

#-----------------------------------------------------------------------
def cmpItems (i1 ,i2 ,cles =[0 ,1 ,2 ,3] , cmp =( lambda x,y : x < y)) :
    assert type(i1) is tuple and len(i1) == 4
    assert type(i2) is tuple and len(i2) == 4
    assert type(cles) is list and (0 < len(cles) <= 4)
    for k in cles:
        if cmp(i1[k],i2[k]) : return True
        elif i1[k] == i2[k] : pass
        else                : return False
    return False

#-----------------------------------------------------------------------
def printListe(t) :
    assert type(t) is list
    for e in t :
        print(e)
    return

def corrige(cles,ordre) :
    annuaire    = [item1, item2, item3, item4, item5, item6]
    triAnnuaire(annuaire,cles,ordre)
    print(cles,end=' ')
    if ordre == croissant : print('croissant')
    else                  : print('décroissant')
    printListe(annuaire)
    print()
    return
    
#-----------------------------------------------------------------------
# 1
cles, ordre = [3, 0, 1, 2], croissant
corrige(cles,ordre)

# 2.
cles, ordre = [3, 0, 2, 1], croissant
corrige(cles,ordre)

# 3.
cles, ordre = [3, 1, 0, 2], croissant
corrige(cles,ordre)

# 4.
cles, ordre = [3, 1, 2, 0], croissant
corrige(cles,ordre)

# 5.
cles, ordre = [3, 2, 0, 1], croissant
corrige(cles,ordre)

# 6.
cles, ordre = [3, 2, 1, 0], croissant
corrige(cles,ordre)

# 7.
cles, ordre = [1, 0, 2, 3], decroissant
corrige(cles,ordre)

# 8.
cles, ordre = [1, 0, 3, 2], decroissant
corrige(cles,ordre)

# 9.
cles, ordre = [1, 2, 0, 3], decroissant
corrige(cles,ordre)

# 10.
cles, ordre = [1, 2, 3, 0], decroissant
corrige(cles,ordre)

# 11.
cles, ordre = [1, 3, 0, 2], decroissant
corrige(cles,ordre)

# 12.
cles, ordre = [1, 3, 2, 0], decroissant
corrige(cles,ordre)

# 13.
cles, ordre = [2, 0, 1, 3], croissant
corrige(cles,ordre)

# 14.
cles, ordre = [2, 0, 3, 1], croissant
corrige(cles,ordre)

# 15.
cles, ordre = [2, 1, 0, 3], croissant
corrige(cles,ordre)

# 16.
cles, ordre = [2, 1, 3, 0], croissant
corrige(cles,ordre)

# 17.
cles, ordre = [2, 3, 0, 1], croissant
corrige(cles,ordre)

# 18.
cles, ordre = [2, 3, 1, 0], croissant
corrige(cles,ordre)

# 19.
cles, ordre = [0, 1, 2, 3], decroissant
corrige(cles,ordre)

# 20.
cles, ordre = [0, 1, 3, 2], decroissant
corrige(cles,ordre)

# 21.
cles, ordre = [0, 2, 1, 3], decroissant
corrige(cles,ordre)

# 22.
cles, ordre = [0, 2, 3, 1], decroissant
corrige(cles,ordre)

# 23.
cles, ordre = [0, 3, 1, 2], decroissant
corrige(cles,ordre)

# 24.
cles, ordre = [0, 3, 2, 1], decroissant
corrige(cles,ordre)

