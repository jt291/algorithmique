# -*- coding: utf-8 -*-
 

#-----------------------------------------------------------------------
def typeNombre(x) :
    """
    ok = typeNombre(x)
    True si x est un nombre, False sinon

    >>> typeNombre(3)
    True
    >>> typeNombre(3.14)
    True
    >>> typeNombre(3.14e-5)
    True
    >>> typeNombre('3.14')
    False
    >>> typeNombre([3])
    False
    """
    
    return type(x) is int or type(x) is float

#-----------------------------------------------------------------------
# piles                       
def pileVide(pile) :
    """
    ok = pileVide(p)
    True si la pile p est vide, False sinon

    >>> pileVide([])
    True
    >>> pileVide([1,2,3])
    False
    """
    assert type(pile) is list
    return pile == []

def sommet(pile) :
    """
    x = sommet(p)
    sommet de la pile p non vide

    >>> sommet([1,2,3])
    3
    """
    assert not pileVide(pile)
    return pile[len(pile)-1]

def empiler(pile,element) :
    """
    empiler(p,e)
    empile e sur la pile p

    >>> p = [1,2,3]
    >>> empiler(p,7)
    >>> p
    [1, 2, 3, 7]
    >>> p = []
    >>> empiler(p,7)
    >>> p
    [7]
    """
    assert type(pile) is list
    pile.append(element)
    return

def depiler(pile) :
    """
    s = depiler(p)
    dépile le sommet s de la pile p non vide

    >>> p = [1,2,3]
    >>> depiler(p)
    3
    >>> depiler(p)
    2
    >>> depiler(p)
    1
    """
    assert not pileVide(pile)
    s = sommet(pile)
    del pile[len(pile)-1]
    return s

#-----------------------------------------------------------------------
# files                       
def fileVide(file) :
    """
    ok = fileVide(f)
    True si la file f est vide, False sinon

    >>> fileVide([])
    True
    >>> fileVide([1,2,3])
    False
    """
    assert type(file) is list
    return file == []

def tete(file) :
    """
    x = tete(f)
    tete de la file f non vide

    >>> tete([1,2,3])
    3
    """
    assert not fileVide(file)
    return file[len(file)-1]

def enfiler(file,element) :
    """
    enfiler(f,e)
    enfile e dans la file f

    >>> f = [1,2,3]
    >>> enfiler(f,7)
    >>> f
    [7, 1, 2, 3]
    >>> f = []
    >>> enfiler(f,7)
    >>> f
    [7]
    """
    assert type(file) is list
    file.insert(0,element)
    return

def defiler(file) :
    """
    t = defiler(f)
    défile la tête t de la file f non vide

    >>> f = [1,2,3]
    >>> defiler(f)
    3
    >>> defiler(f)
    2
    >>> defiler(f)
    1
    """
    assert not fileVide(file)
    t = tete(file)
    del file[len(file)-1]
    return t

#-----------------------------------------------------------------------
# graphes
# un graphe est une liste d'arcs
# un arc est un triplet (noeud1,noeud2,poids)

def Arc(arc) :
    """
    ok = Arc(a)
    True si a est un arc, False sinon

    >>> Arc(('a','b',5))
    True
    >>> Arc(([1,2],[3,4],'p'))
    True
    >>> Arc(('a','b'))
    False
    >>> Arc(['a','b',5])
    False
    """
    ok = True
    if type(arc) is not tuple or len(arc) != 3 :
        ok = False
    return ok

def Graphe(graphe) :
    """
    ok = Graphe(g)
    True si g est un graphe, False sinon
    
    >>> g = [('n1','n1',4),('n1','n2',3)]
    >>> Graphe(g)
    True
    >>> Graphe([1,2,3])
    False
    >>> Graphe(('n1','n2',3))
    False
    """
    if type(graphe) is not list :
        return False
    else :
        for arc in graphe :
            if not Arc(arc) :
                return False
    return True

def adjacents(noeud1,noeud2,graphe) :
    """
    ok = adjacents(n1,n2,g)
    True si n1 et n2 sont 2 noeuds adjacents du graphe g,
    False sinon

    >>> g = [('n1','n2',4),('n2','n3',3)]
    >>> adjacents('n1','n2',g)
    True
    >>> adjacents('n1','n3',g)
    False
    >>> adjacents('n1','n4',g)
    False
    >>> adjacents('n2','n1',g)
    True
    >>> adjacents('n2','n3',g)
    True
    >>> adjacents('n3','n1',g)
    False
    >>> adjacents('n3','n2',g)
    True
    """
    assert Graphe(graphe)
    for (n1,n2,p) in graphe :
        if (n1 == noeud1 and n2 == noeud2) or \
           (n2 == noeud1 and n1 == noeud2) :
            return True
    return False
    
def listeAdjacents(noeud,graphe) :
    """
    arcs = listeAdjacents(n,g)
    liste de tous les noeuds adjacents à un noeund n du graphe g

    >>> g = [('n1','n2',4),('n2','n3',3)]
    >>> listeAdjacents('n1',g)
    [('n1', 'n2', 4)]
    >>> listeAdjacents('n4',g)
    []
    >>> listeAdjacents('n2',g)
    [('n1', 'n2', 4), ('n2', 'n3', 3)]
    >>> listeAdjacents('n3',g)
    [('n2', 'n3', 3)]
    """
    assert Graphe(graphe)
    arcs = []
    for (noeud1,noeud2,poids) in graphe :
        if noeud1 == noeud or noeud2 == noeud :
            arcs.append((noeud1,noeud2,poids))
    return arcs

#-----------------------------------------------------------------------
# chemins dans un graphe
def Chemin(chemin) :
    """
    ok = Chemin(c)
    True si c est un chemin, False sinon

    >>> Chemin((7,['n1','n2','n3']))
    True
    >>> Chemin((7,[]))
    False
    """
    return type(chemin) is tuple    and \
           len(chemin) == 2         and \
           typeNombre(chemin[0])    and \
           type(chemin[1]) is list  and \
           len(chemin[1]) > 0

def extremite(chemin) :
    """
    n = extremite(c)
    dernier noeud n du chemin c

    >>> extremite((7,['n1','n2','n3']))
    'n3'
    """
    assert Chemin(chemin)
    return chemin[1][len(chemin[1])-1]

def cheminsSuivants(chemin,graphe) :
    """
    cs = cheminSuivants(c,g)
    liste des chemins possibles à partir du noeud extrémité d'un chemin c
    d'un graphe g sans repasser par l'un des noeuds du chemin
    
    >>> g = [('n1','n2',4),('n2','n3',3),\
             ('n1','n4',6),('n2','n4',5),\
             ('n2','n4',6)]
    >>> cheminsSuivants((0,['n1']),g)
    [(4, ['n1', 'n2']), (6, ['n1', 'n4'])]
    >>> cheminsSuivants((6,['n1','n4']),g)
    [(11, ['n1', 'n4', 'n2']), (12, ['n1', 'n4', 'n2'])]
    >>> cheminsSuivants((4,['n1','n2']),g)
    [(7, ['n1', 'n2', 'n3']), (9, ['n1', 'n2', 'n4']), (10, ['n1', 'n2', 'n4'])]
    >>> cheminsSuivants((7,['n1','n2','n3']),g)
    []
    >>> cheminsSuivants((9,['n1','n2','n4']),g)
    []
    """    
    assert Chemin(chemin)
    assert Graphe(graphe)
    noeud = extremite(chemin)
    cout = chemin[0]
    route = chemin[1]
    suivants = []
    for arc in listeAdjacents(noeud,graphe) :
        if arc[0] == noeud : noeudSuivant = arc[1]
        else : noeudSuivant = arc[0]
        if noeudSuivant not in route :
            routeSuivante = route + [noeudSuivant]
            coutSuivant = cout + arc[2]
            suivants.append((coutSuivant,routeSuivante))
    return suivants

#-----------------------------------------------------------------------
# recherches de chemins dans un graphe entre noeud1 et noeud2

def profondeur(noeud1,noeud2,graphe,n=100) :
    """
    cs = profondeur(n1,n2,g,n)
    liste des n chemins maximum qui mènent du noeud n1 au noeud n2
    dans le graphe g
    
    >>> graphe = [('s','d',4), ('s','a',3), ('d','e',2), ('d','a',5),\
                  ('a','b',4), ('b','c',4), ('b','e',5), ('e','f',4),\
                  ('f','g',3)]
    >>> profondeur('s','g',graphe)
    [(19, ['s', 'a', 'b', 'e', 'f', 'g']),\
 (17, ['s', 'a', 'd', 'e', 'f', 'g']),\
 (25, ['s', 'd', 'a', 'b', 'e', 'f', 'g']),\
 (13, ['s', 'd', 'e', 'f', 'g'])]
    >>> profondeur('d','b',graphe)
    [(9, ['d', 'a', 'b']), (7, ['d', 'e', 'b']), (11, ['d', 's', 'a', 'b'])]
    """
    assert Graphe(graphe)
    assert type(n) is int and n >= 0
    pile = [(0,[noeud1])]
    chemins = []
    while not pileVide(pile) and n > 0 :
        chemin = depiler(pile)
        noeud = extremite(chemin)
        if noeud == noeud2 :
            chemins.append(chemin)
            n = n - 1
        else :
            pile = pile + cheminsSuivants(chemin,graphe)
    return chemins

def largeur(noeud1,noeud2,graphe,n=100) :
    """
    cs = largeur(n1,n2,g,n)
    liste des n chemins maximum qui mènent du noeud n1 au noeud n2
    dans le graphe g
    
    >>> graphe = [('s','d',4), ('s','a',3), ('d','e',2), ('d','a',5),\
                  ('a','b',4), ('b','c',4), ('b','e',5), ('e','f',4),\
                  ('f','g',3)]
    >>> largeur('s','g',graphe)
    [(13, ['s', 'd', 'e', 'f', 'g']),\
 (19, ['s', 'a', 'b', 'e', 'f', 'g']),\
 (17, ['s', 'a', 'd', 'e', 'f', 'g']),\
 (25, ['s', 'd', 'a', 'b', 'e', 'f', 'g'])]
    >>> largeur('d','b',graphe)
    [(9, ['d', 'a', 'b']), (7, ['d', 'e', 'b']), (11, ['d', 's', 'a', 'b'])]
    """
    assert Graphe(graphe)    
    file = [(0,[noeud1])]
    chemins = []
    while not fileVide(file) and n > 0 :
        chemin = defiler(file)
        noeud = extremite(chemin)
        if noeud == noeud2 :
            chemins.append(chemin)
            n = n - 1
        else :
            file = cheminsSuivants(chemin,graphe) + file
    return chemins

def meilleur(noeud1,noeud2,graphe,n=100) :
    """
    cs = meilleur(n1,n2,g,n)
    liste des n chemins maximum qui mènent du noeud n1 au noeud n2
    dans le graphe g
    
    >>> graphe = [('s','d',4), ('s','a',3), ('d','e',2), ('d','a',5),\
                  ('a','b',4), ('b','c',4), ('b','e',5), ('e','f',4),\
                  ('f','g',3)]
    >>> meilleur('s','g',graphe)
    [(13, ['s', 'd', 'e', 'f', 'g']),\
 (17, ['s', 'a', 'd', 'e', 'f', 'g']),\
 (19, ['s', 'a', 'b', 'e', 'f', 'g']),\
 (25, ['s', 'd', 'a', 'b', 'e', 'f', 'g'])]
    >>> meilleur('d','b',graphe)
    [(7, ['d', 'e', 'b']), (9, ['d', 'a', 'b']), (11, ['d', 's', 'a', 'b'])]
    >>> meilleur('s','g',graphe,1)
    [(13, ['s', 'd', 'e', 'f', 'g'])]
    >>> meilleur('s','g',graphe,2)
    [(13, ['s', 'd', 'e', 'f', 'g']), (17, ['s', 'a', 'd', 'e', 'f', 'g'])]
    """
    assert Graphe(graphe)    
    file = [(0,[noeud1])]
    chemins = []
    while not fileVide(file) and n > 0 :
        chemin = defiler(file)
        noeud = extremite(chemin)
        if noeud == noeud2 :
            chemins.append(chemin)
            n = n - 1
        else :
            file = cheminsSuivants(chemin,graphe) + file
            file.sort(reverse=True)
    return chemins


#-----------------------------------------------------------------------
# problème du réseau routier
depart, arrivee = 's', 'g'

def reseau(noeud) :
    """
    >>> reseau('a')
    [('s', 'a', 3), ('d', 'a', 5), ('a', 'b', 4)]
    >>> reseau('s')
    [('s', 'd', 4), ('s', 'a', 3)]
    >>> reseau('c')
    [('b', 'c', 4)]
    """
    g = [('s','d',4),\
         ('s','a',3),\
         ('d','e',2),\
         ('d','a',5),\
         ('a','b',4),\
         ('b','c',4),\
         ('b','e',5),\
         ('e','f',4),\
         ('f','g',3)]
    return listeAdjacents(noeud,g)

#-----------------------------------------------------------------------
# problème des vases
depart, arrivee = (0,0), (4,0)

def capacite() :
    return (8,5)

def vider(eprouvette, etat) :
    if eprouvette == 0 :
        etatFinal = (0,etat[1])
    else :
        etatFinal = (etat[0],0)
    return etatFinal

def remplir(eprouvette, etat) :
    if eprouvette == 0 :
        etatFinal = (capacite()[0],etat[1])
    else :
        etatFinal = (etat[0],capacite()[1])
    return etatFinal

def transvaser(eprouvette, etat) :
    if eprouvette == 0 :
        reste = capacite()[1] - etat[1]
        if etat[0] <= reste :
            etatFinal = (0,etat[1]+etat[0])
        else :
            etatFinal = (etat[0]-reste,capacite()[1])
    else :
        reste = capacite()[0] - etat[0]
        if etat[1] <= reste :
            etatFinal = (etat[0]+etat[1],0)
        else :
            etatFinal = (capacite()[0],etat[1]-reste)
    return etatFinal

def vases(noeud) :
    """
    >>> vases((0,0))
    [((0, 0), (0, 5), 1), ((0, 0), (8, 0), 1)]
    >>> vases((8,0))
    [((8, 0), (3, 5), 1), ((8, 0), (8, 5), 1), ((8, 0), (0, 0), 1)]
    >>> vases((0,5))
    [((0, 5), (5, 0), 1), ((0, 5), (8, 5), 1), ((0, 5), (0, 0), 1)]
    """
    suivants = []
    if noeud[1] != 0 and noeud[0] != capacite()[0] :
        noeudSuivant = transvaser(1,noeud)
        suivants.append((noeud,noeudSuivant,1))
    if noeud[0] != 0 and noeud[1] != capacite()[1] :
        noeudSuivant = transvaser(0,noeud)
        suivants.append((noeud,noeudSuivant,1))
    if noeud[1] != capacite()[1] :
        noeudSuivant = remplir(1,noeud)
        suivants.append((noeud,noeudSuivant,1))
    if noeud[0] != capacite()[0] :
        noeudSuivant = remplir(0,noeud)
        suivants.append((noeud,noeudSuivant,1))
    if noeud[1] != 0 :
        noeudSuivant = vider(1,noeud)
        suivants.append((noeud,noeudSuivant,1))
    if noeud[0] != 0 :
        noeudSuivant = vider(0,noeud)
        suivants.append((noeud,noeudSuivant,1))
    return suivants


#-----------------------------------------------------------------------
# jeu du taquin
depart, arrivee = [[3,1],[0,2]], [[1,2],[3,0]]

def carreauVide(jeu) :
    n = len(jeu)
    ok = False
    i = 0
    while i < n and not ok :
        if 0 in jeu[i] :
            j = 0
            while j < n and not ok :
                if jeu[i][j] == 0 : ok = True
                else : j = j + 1
        else : i = i + 1
    return (i,j)

def permuterVide(jeu,pos1,pos2) :
    n = len(jeu)
    jeu1 = []
    for i in range(n) :
        jeu1.append([])
        for j in range(n) :
            jeu1[i].append(jeu[i][j])            
    jeu1[pos1[0]][pos1[1]], jeu1[pos2[0]][pos2[1]] = jeu1[pos2[0]][pos2[1]], jeu1[pos1[0]][pos1[1]]
    return jeu1
    
def taquin(jeu) :
    """
    >>> jeu = [[3,1],[0,2]]
    >>> taquin(jeu)
    [([[3, 1], [0, 2]], [[0, 1], [3, 2]], 1),\
 ([[3, 1], [0, 2]], [[3, 1], [2, 0]], 1)]
    >>> jeu = [[2,1,8],[6,0,3],[7,5,4]]
    >>> taquin(jeu)
    [([[2, 1, 8], [6, 0, 3], [7, 5, 4]], [[2, 0, 8], [6, 1, 3], [7, 5, 4]], 1),\
 ([[2, 1, 8], [6, 0, 3], [7, 5, 4]], [[2, 1, 8], [6, 5, 3], [7, 0, 4]], 1),\
 ([[2, 1, 8], [6, 0, 3], [7, 5, 4]], [[2, 1, 8], [0, 6, 3], [7, 5, 4]], 1),\
 ([[2, 1, 8], [6, 0, 3], [7, 5, 4]], [[2, 1, 8], [6, 3, 0], [7, 5, 4]], 1)]
    """
    n = len(jeu)
    (i0,j0) = carreauVide(jeu)
    suivants = []

    (i1,j1) = (max(0,i0-1),j0)
    jeu1 = permuterVide(jeu,(i0,j0),(i1,j1))
    if jeu1 != jeu : suivants.append((jeu,jeu1,1))

    (i1,j1) = (min(i0+1,n-1),j0)
    jeu1 = permuterVide(jeu,(i0,j0),(i1,j1))
    if jeu1 != jeu : suivants.append((jeu,jeu1,1))

    (i1,j1) = (i0,max(0,j0-1))
    jeu1 = permuterVide(jeu,(i0,j0),(i1,j1))
    if jeu1 != jeu : suivants.append((jeu,jeu1,1))

    (i1,j1) = (i0,min(j0+1,n-1))
    jeu1 = permuterVide(jeu,(i0,j0),(i1,j1))
    if jeu1 != jeu : suivants.append((jeu,jeu1,1))

    return suivants


#-----------------------------------------------------------------------
def meilleurFct(noeud1,noeud2,f,n=100) :
    """
    cs = meilleurf(n1,n2,f,n)
    liste des n chemins maximum qui mènent du noeud n1 au noeud n2

    >>> depart, arrivee = 's', 'g'
    >>> meilleurFct(depart,arrivee,reseau,1)
    [(13, ['s', 'd', 'e', 'f', 'g'])]
    >>> meilleurFct('d','b',reseau,1)
    [(7, ['d', 'e', 'b'])]
    >>> depart, arrivee = (0,0), (4,0)
    >>> meilleurFct(depart,arrivee,vases,5)
    [(12, [(0, 0), (0, 5), (5, 0), (5, 5), (8, 2), (0, 2), (2, 0), (2, 5), (7, 0), (7, 5), (8, 4), (0, 4), (4, 0)]),\
 (13, [(0, 0), (8, 0), (3, 5), (3, 0), (0, 3), (8, 3), (6, 5), (6, 0), (1, 5), (1, 0), (0, 1), (8, 1), (4, 5), (4, 0)]),\
 (14, [(0, 0), (8, 0), (3, 5), (0, 5), (5, 0), (5, 5), (8, 2), (0, 2), (2, 0), (2, 5), (7, 0), (7, 5), (8, 4), (0, 4), (4, 0)]),\
 (14, [(0, 0), (8, 0), (8, 5), (0, 5), (5, 0), (5, 5), (8, 2), (0, 2), (2, 0), (2, 5), (7, 0), (7, 5), (8, 4), (0, 4), (4, 0)]),\
 (15, [(0, 0), (0, 5), (5, 0), (8, 0), (3, 5), (3, 0), (0, 3), (8, 3), (6, 5), (6, 0), (1, 5), (1, 0), (0, 1), (8, 1), (4, 5), (4, 0)])]
    >>> depart, arrivee = [[3,1],[0,2]], [[1,2],[3,0]]
    >>> meilleurFct(depart,arrivee,taquin,10)
    [(3, [[[3, 1], [0, 2]], [[0, 1], [3, 2]], [[1, 0], [3, 2]], [[1, 2], [3, 0]]]),\
 (9, [[[3, 1], [0, 2]], [[3, 1], [2, 0]], [[3, 0], [2, 1]], [[0, 3], [2, 1]],\
 [[2, 3], [0, 1]], [[2, 3], [1, 0]], [[2, 0], [1, 3]], [[0, 2], [1, 3]],\
 [[1, 2], [0, 3]], [[1, 2], [3, 0]]])]
    """
    file = [(0,[noeud1])]
    chemins = []
    while not fileVide(file) and n > 0 :
        chemin = defiler(file)
        noeud = extremite(chemin)
        if noeud == noeud2 :
            chemins.append(chemin)
            n = n - 1
        else :
            file = cheminsSuivantsFct(chemin,f) + file
            file.sort(reverse=True)
    return chemins

def cheminsSuivantsFct(chemin,f) :
    assert Chemin(chemin)
    noeud = extremite(chemin)
    cout = chemin[0]
    route = chemin[1]
    suivants = []
    for arc in f(noeud) :
        if arc[0] == noeud : noeudSuivant = arc[1]
        else : noeudSuivant = arc[0]
        if noeudSuivant not in route :
            routeSuivante = route + [noeudSuivant]
            coutSuivant = cout + arc[2]
            suivants.append((coutSuivant,routeSuivante))
    return suivants

#-----------------------------------------------------------------------
if __name__ == '__main__' :
    import doctest
    doctest.testmod()
