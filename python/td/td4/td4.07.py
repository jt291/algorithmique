# -*- coding: utf-8 -*-
 
# s[i] = x
l = [1,2,3,4,5,6]
n, x = 2, 0
print(l,'[',n,'] = ',x,' : ',l,' -> ',sep='',end='')
l[n] = x
print(l)

# s[i:j] = t
l = [1,2,3,4,5,6]
i, j = 1, 3
t = [-4, -5]
print(l,'[',i,':',j,'] = ',t,' : ',l,' -> ',sep='',end='')
l[i:j] = t
print(l)

# del s[i:j]	same as s[i:j] = []
l = [1,2,3,4,5,6]
i, j = 1, 3
print('del ',l,'[',i,':',j,'] : ',l,' -> ',sep='',end='')
del l[i:j]
print(l)

# s[i:j:k] = t	the elements of s[i:j:k] are replaced by those of t	(1)
l = [1,2,3,4,5,6]
i, j, k = 1, 6, 2
t = [-4,-5,-6]
print(l,'[',i,':',j,':',k,'] = ',t,' : ',l,' -> ',sep='',end='')
l[i:j:k] = t
print(l)

# del s[i:j:k]	removes the elements of s[i:j:k] from the list
l = [1,2,3,4,5,6]
i, j, k = 1, 6, 2
print('del ',l,'[',i,':',j,':',k,'] : ',l,' -> ',sep='',end='')
del l[i:j:k]
print(l)

# s.append(x)
l = [1,2,3,4,5,6]
x = 0
print(l,'.append(',x,') : ',l,' -> ',sep='',end='')
l.append(x)
print(l)

# s.extend(t)	extends s with the contents of t (same as s[len(s):len(s)] = t)
l = [1,2,3]
t = [7,8,9]
print(l,'.extend(',t,') : ',l,' -> ',sep='',end='')
l.extend(t)
print(l)

# s.insert(i, x)
l = [4,5,6]
i, x = 1, -4
print(l,'.insert(',i,',',x,') -> ',sep='',end='')
l.insert(i,x)
print(l)

# s.pop([i])
l = [2,3,4,5,6]
i = 1
print(l,'.pop(',i,') : ',l,' -> ',sep='',end='')
l.pop(i)
print(l)

# s.remove(x)
l = [2,3,4,5,4,3]
x = 4
print(l,'.remove(',x,') : ',l,' -> ',sep='',end='')
l.remove(x)
print(l)

# s.reverse()
l = [1,2,3]
print(l,'.reverse() : ',l,' -> ',sep='',end='')
l.reverse()
print(l)

# s.sort()
l = [8,5,9,2,0,1,5]
print(l,'.sort() : ',l,' -> ',sep='',end='')
l.sort()
print(l)
