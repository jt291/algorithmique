# -*- coding: utf-8 -*-
 
a, b, c = 1, 0, 1

# circuit 1
s = (a and not b) or (b and not a)
print('circuit 1 :',a,b,'->',int(s))

# circuit 2
s = not (not (a and not b) and not (b and not a))
print('circuit 2 :',a,b,'->',int(s))

# circuit 3
s = (a and not b) or (not a and b)
t = (not a) and b
print('circuit 3 :',a,b,'->',int(s),int(t))

# circuit 4
s = (a != (b != c))
t = (b and c) or (a and (b != c))
print('circuit 4 :',a,b,'->',int(s),int(t))

# circuit 5
s = (a and c) or (b and c) or (a and b)
print('circuit 5 :',a,b,c,'->',int(s))

# circuit 6
u = a and (not b) and c
s = (a and not c) or u
t = (b and c) or u
print('circuit 6 :',a,b,c,'->',int(s),int(t))

# circuit 7
u = not a and not b and not c
v = a and not b and not c
w = a and b and not c
s = not (not u and not v and not w)
print('circuit 7 :',a,b,c,'->',int(s))

# circuit 8
s7 = a and b and c
s6 = a and b and not c
s5 = a and not b and c
s4 = a and not b and not c
s3 = not a and b and c
s2 = not a and b and not c
s1 = not a and not b and c
s0 = not a and not b and not c
print('circuit 8 :',a,b,c,'->',int(s0),int(s1),int(s2),int(s3),int(s4),int(s5),int(s6),int(s7))
