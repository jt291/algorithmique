# -*- coding: utf-8 -*-
 
#-----------------------------------------------------------------------
def triSelection(t,debut,fin):
    assert type(t) is list
    assert 0 <= debut <= fin < len(t)
    while debut < fin:
        mini = minimum(t,debut,fin)
        t[debut],t[mini] = t[mini],t[debut]
        debut = debut + 1
    return

#-----------------------------------------------------------------------
def minimum(t,debut,fin):
    assert type(t) is list
    assert 0 <= debut <= fin < len(t)
    mini = debut
    for j in range(debut+1,fin+1):
        if t[j] < t[mini]: mini = j
        print(j,end=' ')
    print()
    return mini


#-----------------------------------------------------------------------
# tri par sélection 1 : échanges de valeurs en O(n)
solution1 = """1.
Les échanges de valeurs interviennent dans l'instruction
    t[debut],t[mini] = t[mini],t[debut]
qui est présente dans le corps de la boucle
    while debut < fin:
        mini = minimum(t,debut,fin)
        t[debut],t[mini] = t[mini],t[debut]
        debut = debut + 1
Or, on passe (fin-debut) fois dans cette boucle, soit
l'ordre de grandeur du nombre d'éléments à trier : O(n).
"""
print(solution1)

#-----------------------------------------------------------------------
# tri par sélection 2 : comparaisons entre éléments en O(n^2)
solution2 = """2.
Les comparaisons entre éléments (t[j] < t[mini]) interviennent
dans le corps de la boucle de la fonction minimum 
    for j in range(debut+1,fin+1):
        if t[j] < t[mini]: mini = j
On passe (fin-debut) fois dans cette boucle,
soit l'ordre de grandeur du nombre d'éléments à comparer à chaque
appel de la fonction minimum. La fonction minimum est elle-même
appelée dans le corps de la boucle
    while debut < fin:
        mini = minimum(t,debut,fin)
        t[debut],t[mini] = t[mini],t[debut]
        debut = debut + 1
Au premier passage, on effectue n comparaisons, (n-1) au 2ème passage, (n-2)
au troisième passage et ainsi de suite, soit en tout s comparaisons avec
s = n + (n-1) + (n-2) + ... + 1.
s est donc la somme des n premiers nombres entiers, à savoir
s = n*(n+1)/2, donc de l'ordre de n^2 : O(n^2).
"""
print(solution2)
