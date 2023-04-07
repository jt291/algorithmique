# -*- coding: utf-8 -*-
 
# x in s
x = 3
s = (1,2,3,4)
if x in s:
    print(x,'in',s,':',x in s)
else:
    print(x,'not in',s,':',x not in s)

# x not in s
x = 0
s = (1,2,3,4)
if x in s:
    print(x,'in',s,':',x in s)
else:
    print(x,'not in',s,':',x not in s)

# s1 + s2
s1 = (1,2,3)
s2 = (4,5)
print(s1,'+',s2,'=',s1+s2,'!=',s2,'+',s1,'=',s2+s1,':',s1+s2 != s2+s1)

# s*n, n*s
n = 3
s = (1,2)
print(s,'*',n,'=',s*n,'=',n,'*',s,'=',n*s,':',s*n == n*s)

# s[i]
s = (1,2,3)
for i in range(len(s)):
    print(s,'[',i,'] =',s[i])

# s[i:j:step]
s = (0,1,2,3,4,5,6,7,8,9)
print('nombres pairs   :',s[0:10:2])
print('nombres impairs :',s[1:10:2])

# len(s)
s1 = (1,2,3)
s2 = (4,5)
print('len(',s1+s2,') =',len(s1+s2),'=',len(s1),'+',len(s2),'= len(',s1,') + len(',s2,')')

# min(s)
s = (6,4,7,9,2,1,0,3,5,8)
print('min(',s,') = ',min(s))

# max(s)
s = (6,4,7,9,2,1,0,3,5,8)
print('max(',s,') = ',max(s))
