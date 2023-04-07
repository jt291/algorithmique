# -*- coding: utf-8 -*-
 
# opérateur booléen 1 : ou exclusif
for a in [0,1]:
    for b in [0,1]:
        y = (a and not b) or (not a and b)
        print('ou exclusif :',a,b,'->',int(y))
print()

# opérateur booléen 2 : non ou
for a in [0,1]:
    for b in [0,1]:
        y = not (a or b)
        print('non ou      :',a,b,'->',int(y))
print()

# opérateur booléen 3 : non et
for a in [0,1]:
    for b in [0,1]:
        y = not (a and b)
        print('non et      :',a,b,'->',int(y))
print()

# opérateur booléen 4 : implication
for a in [0,1]:
    for b in [0,1]:
        y = not a or b
        print('implication :',a,b,'->',int(y))
print()

# opérateur booléen 5 : équivalence
for a in [0,1]:
    for b in [0,1]:
        y = (not a or b) and (not b or a)
        print('équivalence :',a,b,'->',int(y))
print()
