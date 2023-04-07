Cette archive est la version v6 des différents documents
accompagnant le cours d'Initiation à l'algorithmique
du semestre S1 de l'[Ecole nationale d'ingénieurs de Brest](https://www.enib.fr) (ENIB).

Une fois décompressée dans le répertoire voulu :

	$ tar zxvf info-S1-v6-1.tar.gz

se déplacer dans le sous-répertoire `v6/` pour la consulter :

	$ cd v6


Cette archive s'organise autour de 3 répertoires :

	v6$ ls
	pdf/  python/  tex/

Le répertoire `pdf/` contient tous les fichiers pdf
du cours d'algorithmique : cours, td, ds, corrigés...
Le répertoire `python/` contient les codes sources en langage
Python (3.2.2) des réponses aux TD et aux contrôles.
Le répertoire `tex/` contient tous les codes sources LaTeX
permettant de générer l'ensemble des fichiers du répertoire `pdf/`.

## Le répertoire `pdf/`
Ce répertoire contient 93 fichiers pdf organisés en 6 sous-répertoires :

	v6/pdf$ ls
	controles/  cours/  mvr/  questionnements/  syllabus/  td/

## Le répertoire `python/`
Ce répertoire contient 223 fichiers Python organisés en 2 sous-répertoires :

	v6/python$ ls
	controles/  td/

L'ensemble des fichiers Python a été testé avec la version 3.2.2
de l'interpréteur Python :

	$ python
	Python 3.2.2 (default, Nov 21 2011, 16:50:59)
	[GCC 4.6.2] on linux2
	Type "help", "copyright", "credits" or "license" for more information.
	>>> quit()

Avec la version 2.7.2, il y a les problèmes connus de l'instruction « print »
qui sont apparus lors du passage de la version 2 à la version 3 de Python,
en particulier avec les arguments « sep », « end » et « file » de la fonction
« print » en Python 3.

Pour les accros de la version 2 :

`print(un,deux,trois,sep=separ,end=fin,file=fichier)` en Python 3

donne

`print >>fichier, separ.join((str(un),str(deux),str(trois))),; fichier.write(fin)` en Python 2

Le cas par défaut

`print(1,2,3,sep=" ",end="\n",file=sys.stdout)` en Python 3

donne

`print 1,2,3` en Python 2


## Le répertoire `tex/`
Ce répertoire contient 156 fichiers LaTeX organisés en 6 répertoires principaux
et 2 répertoires utilitaires (`fig/` et `macros/`) :

	v6/tex$ ls
	README  controles/  cours/  fig/  macros/  makefile  mvr/  questionnements/  syllabus/  td/

Pour regénérer l'ensemble des fichiers pdf, se placer dans le répertoire `v6/tex/`
et lancer la commande `make all`. Cela peut prendre plusieurs minutes :

	v6/tex$ time make all
	...
	real	7m15.641s
	user	6m34.174s
	sys		0m39.011s

