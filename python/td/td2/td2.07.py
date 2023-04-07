# -*- coding: utf-8 -*-
 
# loi de De Morgan 1
a, b = 0, 0
y = (not (a or b)) == (not a and not b)
print(a,b,'->',int(y))
a, b = 0, 1
y = (not (a or b)) == (not a and not b)
print(a,b,'->',int(y))
a, b = 1, 0
y = (not (a or b)) == (not a and not b)
print(a,b,'->',int(y))
a, b = 1, 1
y = (not (a or b)) == (not a and not b)
print(a,b,'->',int(y))
print()

# loi de De Morgan 2
a, b = 0, 0
y = (not (a and b)) == (not a or not b)
print(a,b,'->',int(y))
a, b = 0, 1
y = (not (a and b)) == (not a or not b)
print(a,b,'->',int(y))
a, b = 1, 0
y = (not (a and b)) == (not a or not b)
print(a,b,'->',int(y))
a, b = 1, 1
y = (not (a and b)) == (not a or not b)
print(a,b,'->',int(y))
