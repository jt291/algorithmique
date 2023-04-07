# -*- coding: utf-8 -*-
 
# circuit 1
for a in [0,1] :
    for b in [0,1] :
        for c in [0,1] :
            s = (a and not b) or (b and not a)
            print(a, b, c, ':', int(s))
print()

# circuit 2
for a in [0,1] :
    for b in [0,1] :
        s = not (not (a and not b) and not (b and not a))
        print(a, b, ':', int(s))
print()

# circuit 3
for a in [0,1] :
    for b in [0,1] :
        s = (a and not b) or (not a and b)
        t = (not a) and b
        print(a, b, ':', int(s), int(t))
print()

# circuit 4
for a in [0,1] :
    for b in [0,1] :
        for c in [0,1] :
            s = (a != (b != c))
            t = (b and c) or (a and (b != c))
            print(a, b, c, ':', int(s), int(t))
print()

# circuit 5
for a in [0,1] :
    for b in [0,1] :
        for c in [0,1] :
            s = not (not (a and b) and not (a and c) and not (b and c))
            print(a, b, c, ':', int(s))
print()

# circuit 6
for a in [0,1] :
    for b in [0,1] :
        for c in [0,1] :
            u = not a and not b and not c
            v = a and not b and not c
            w = a and b and not c
            s = not (not u and not v and not w)
            print(a, b, c, ':', int(s))
print()

# circuit 7
for a in [0,1] :
    for b in [0,1] :
        for c in [0,1] :
            u = (b and not c) or (not b and c)
            s = (a and not u) or (not a and u)
            t = (b and c) or (a and u)
            print(a, b, c, ':', int(u), int(s), int(t))
print()

# circuit 8
for a in [0,1] :
    for b in [0,1] :
        for c in [0,1] :
            s7 = a and b and c
            s6 = a and b and not c
            s5 = a and not b and c
            s4 = a and not b and not c
            s3 = not a and b and c
            s2 = not a and b and not c
            s1 = not a and not b and c
            s0 = not a and not b and not c
            print(a, b, c, ':', int(s0), int(s1), int(s2), int(s3), int(s4), int(s5), int(s6), int(s7))
