# -*- coding: utf-8 -*-
 
jour, h = 'mardi', 13.5
if h < 8 or (13 < h < 14) or h > 17 : guichet = 'fermé'
else:
    if jour == 'dimanche' : guichet = 'fermé'
    else:
        if jour == 'samedi' and (h > 13 or h < 8) : guichet = 'fermé'
        else: guichet = 'ouvert'
print(jour,h,'->',guichet)
