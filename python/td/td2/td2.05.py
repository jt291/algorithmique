# -*- coding: utf-8 -*-
 
# opérateur booléen 1 : ou exclusif
a, b = 1, 0
y = (a and not b) or (not a and b)
print('ou exclusif :',a,b,'->',int(y))

# opérateur booléen 2 : non ou
a, b = 1, 0
y = not (a or b)
print('non ou      :',a,b,'->',int(y))

# opérateur booléen 3 : non et
a, b = 1, 0
y = not (a and b)
print('non et      :',a,b,'->',int(y))

# opérateur booléen 4 : implication
a, b = 1, 0
y = not a or b
print('implication :',a,b,'->',int(y))

# opérateur booléen 5 : équivalence
a, b = 1, 0
y = (not a or b) and (not b or a)
print('équivalence :',a,b,'->',int(y))
