#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path, sys, random

#-----------------------------------------------------------------------
def qcm(titre='Essai', f='essai.qcm', n=2, latex='xelatex') :
    """
    qf = genererQcm(titre,f,n,latex)
    génère avec latex un fichier pdf de n questionnaires à partir du fichier f
    d'extension .qcm
    """
    
    nomSource   = os.path.splitext(f)[0]
    nomEnonce   = 'qcm-'+nomSource+'.tex'
    nomCorrige  = 'c-qcm-'+nomSource+'.tex'

    fSource     = open(f)
    fEntete     = open('entete-qcm.tex')
    source = fSource.read()
    entete = fEntete.read()
    fSource.close()
    fEntete.close()

    lsource = eval(source)
    couleurTrue, couleurFalse = 'red!99', 'lightgray!49'
    couleur = couleurFalse
    for i in range(len(lsource)) :
        question, reponses = lsource[i]
        lsource[i][0] = '\\item ' + question + '\\hrulefill\n'
        for j in range(len(reponses)) :
            if j == 0 : couleur = couleurTrue
            lsource[i][1][j] = '\t\\item \\begin{minipage}[t]{0.8\\textwidth}' + reponses[j] + '\\end{minipage}\\hfill\colorbox{' + couleur + '}{~~}\n'
            couleur = couleurFalse                

    enonce  = entete
    corrige = entete
    for i in range(n) :
        lmix = [e for e in lsource]
        lmix = mixerItems(lmix)
        for j in range(len(lmix)) :
            lmix[j][1] = mixerItems(lmix[j][1])

        enonce  += '\\entete{' + titre + '}\n\n' + '\\begin{enumerate}\n'
        corrige += '\\entete{' + titre + '}\n\n' + '\\begin{enumerate}\n'
        for [question, reponses] in lmix :
            enonce  += question + '\t\\begin{enumerate}\n'
            corrige += question + '\t\\begin{enumerate}\n'
            for rep in reponses :
                enonce  += rep.replace(couleurTrue,couleurFalse)
                corrige += rep
            enonce  += '\t\\end{enumerate}\\vspace*{3mm}\n\n'
            corrige += '\t\\end{enumerate}\\vspace*{3mm}\n\n'

        enonce  += '\\end{enumerate}\n\n\\newpage\n'
        corrige += '\\end{enumerate}\n\n\\newpage\n'

    enonce  += '\\end{document}\n'
    corrige += '\\end{document}\n'

    fEnonce  = open(nomEnonce,'w')
    fCorrige = open(nomCorrige,'w')
    fEnonce.write(enonce)
    fCorrige.write(corrige)
    fEnonce.close()    
    fCorrige.close()

    return genererPdf(nomEnonce,nomCorrige,latex)

#-----------------------------------------------------------------------
def genererPdf(nomEnonce,nomCorrige,latex='xelatex') :
    commande  = latex + ' ' + nomEnonce + '; '
    commande += latex + ' ' + nomCorrige +'; '
    commande += 'rm -f *.*~ *.aux *.log *.maf *.mtc* *.out *.thm'
    return os.system(commande)

#-----------------------------------------------------------------------
def selectionAleatoire(t) :
    assert type(t) is list
    position = random.randrange(len(t))
    valeur = t.pop(position)
    return valeur, t

#-----------------------------------------------------------------------
def mixerItems(tIn) :
    tOut = []
    while len(tIn) > 0 :
        valeur, tIn = selectionAleatoire(tIn)
        tOut .append(valeur)
    return tOut

#-----------------------------------------------------------------------
arguments = sys.argv
if len(arguments) == 5 :
    latex = arguments[4]
    n = int(arguments[3])
    f = arguments[2]
    titre = arguments[1]
    qcm(titre,f,n,latex)    
elif len(arguments) == 4 :
    n = int(arguments[3])
    f = arguments[2]
    titre = arguments[1]
    qcm(titre,f,n)    
elif len(arguments) == 3 :
    f = arguments[2]
    titre = arguments[1]
    qcm(titre,f)    
elif len(arguments) == 2 :
    titre = arguments[1]
    qcm(titre)
elif len(arguments) == 1 :
    qcm()
else :
    usage = '''usage : $ python qcm.py titre f n latex
    titre : titre du qcm ('Essai' par défaut)
    f     : fichier source d'extension .qcm (essai.qcm par défaut)
    n     : nombre de copies (40 par défaut)
    latex : exécutable LaTeX (xelatex par défaut)'''
    print(usage)


