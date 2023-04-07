# -*- coding: utf-8 -*-
 
age = 9.5
if    6 <= age <  8 : categorie = 'poussin'
elif  8 <= age < 10 : categorie = 'pupille'
elif 10 <= age < 12 : categorie = 'minime'
elif 12 <= age < 14 : categorie = 'cadet'
else                : categorie = 'autre'
print(age,'->',categorie)
