# -*- coding: utf-8 -*-
 
age = 25
sexe = 'f'
if age > 18 :
    if sexe == 'm' : impot = True
    elif  age < 35 : impot = True
    else           : impot = False
else : impot = False
print(age,sexe,'->',impot)
