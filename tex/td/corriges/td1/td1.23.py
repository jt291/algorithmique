# -*- coding: utf-8 -*-
 
"""
Imaginons l'algorithme de tracé suivant :

    avance de 2 pas,
    tourne à gauche de 90°,
    avance de 3 pas,
    tourne à gauche de 90°,
    avance de 4 pas,
    tourne à gauche de 90°,
    avance de 5 pas,
    tourne à gauche de 90°,
    avance de 6 pas.

validité : on doit au moins vérifier que la figure obtenue à toutes
    les caractéristiques recherchées : spirale rectangulaire de
    5 côtés, le plus petit côté faisant 2 pas de long et chaque 
    côté fait un pas de plus que le précédent.

robustesse : cet algorithme suppose qu'on a suffisamment de place pour
    tracer une spirale (le dernier côté fait 6 pas de long);
    s'il fonctionne correctement sur une plage,
    il ne fonctionnera certainement plus dans un placard.

réutilisabilité : il existe une infinité de spirales rectangulaires
    qui ont les caractéristiques attendues; il suffit de penser
    à changer l'orientation initiale ou la longueur du pas par exemple. 
    On ne pourra donc pas utiliser l'algorithme tel quel dans toutes les
    configurations : il aurait fallu paramétrer l'angle de rotation et la
    longueur du pas.

complexité : on peut la caractériser par le nombre de pas : 
    2 + 3 + 4 + 5 + 6 = 20 pas.

efficacité : si la complexité se calcule en nombre de pas comme
    ci-dessus, on pourrait imaginer par exemple que la fréquence des
    pas soit plus grande (« fréquence d'horloge ») ou que 
    5 personnes prennent en charge chacune un côté de la spirale 
    pour gagner du temps (« système multi-processeurs »).
"""
