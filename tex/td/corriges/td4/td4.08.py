# -*- coding: utf-8 -*-
 
# del s[i:j] et s[i:j] = []
s = [1,2,3,4,5,6]
l = [1,2,3,4,5,6]
i, j = 1, 3
del s[i:j]
l[i:j] = []
print('del s[i:j] et s[i:j] = [] :',l == s)

# s.append(x) et s[len(s):len(s)] = [x]
s = [1,2,3,4,5,6]
l = [1,2,3,4,5,6]
x = 0
s.append(x)
l[len(l):len(l)] = [x]
print('s.append(x) et s[len(s):len(s)] = [x] :',l == s)

# s.extend(x) et s[len(s):len(s)] = x
s = [1,2,3,4,5,6]
l = [1,2,3,4,5,6]
x = [-3,-4]
s.extend(x)
l[len(l):len(l)] = x
print('s.extend(x) et s[len(s):len(s)] = x :',l == s)

# s.insert(i,x) et s[i:i] = [x]
s = [1,2,3,4,5,6]
l = [1,2,3,4,5,6]
x = -3
i = 1
s.insert(i,x)
l[i:i] = [x]
print('s.insert(i,x) et s[i:i] = [x] :',l == s)

# s.remove(x) et del s[s.index(x)]
s = [1,2,3,4,5,6]
l = [1,2,3,4,5,6]
x = 3
s.remove(x)
del l[l.index(x)]
print('s.remove(x) et del s[s.index(x)] :',l == s)

# s.pop(i) et x = s[i]; del s[i]
s = [4,5,6,7]
l = [4,5,6,7]
i = 2
s.pop(i)
x = l[i]; del l[i]
print('s.pop(i) et x = s[i]; del s[i] :',l == s)
