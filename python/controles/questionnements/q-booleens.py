# -*- coding: utf-8 -*-
 
def table(s0,t0,u0,v0,z0) :
    
    print('a','b','c','|','s','t','u','v','|','z')
    print('----------------|--')
    for a in [0,1] :
        for b in [0,1] :
            for c in [0,1] :
                s = eval(s0)
                t = eval(t0)
                u = eval(u0)
                v = eval(v0)
                z = eval(z0)
                print(a,b,c,'|',int(s),int(t),int(u),int(v),'|',int(z))
    print()
    return

#-----------------------------------------------------------------------
# 1
print('1.')
s = 'not a or b'
t = 'not (not b or c)'
u = 's or t'
v = 'not c or not a'
z = 'not u or v'
table(s,t,u,v,z)

# 2
print('2.')
s = 'not a or b'
t = 'not b or not c'
u = 's and t'
v = '(not c) != (not a)'
z = 'not u or v'
table(s,t,u,v,z)

# 3
print('3.')
s = 'not (a != (not b))'
t = 'b and c'
u = 'not s or t'
v = '(not c) != (not a)'
z = 'not u or v'
table(s,t,u,v,z)

# 4
print('4.')
s = 'not a or not b'
t = 'b or c'
u = 's and t'
v = 'not (c or not a)'
z = 'not u or v'
table(s,t,u,v,z)

# 5
print('5.')
s = 'a or not b'
t = 'not b or c'
u = 's and t'
v = 'not c or a'
z = 'not u or v'
table(s,t,u,v,z)

# 6
print('6.')
s = 'not a or b'
t = 'not (not b or not c)'
u = 's or t'
v = '(not c) != (not a)'
z = 'not u or v'
table(s,t,u,v,z)

# 7
print('7.')
s = 'a and b'
t = 'b and c'
u = 's != t'
v = 'c or not a'
z = 'not u or v'
table(s,t,u,v,z)

# 8
print('8.')
s = 'not a or b'
t = 'not b or not c'
u = 's and t'
v = 'c or not a'
z = 'not u or v'
table(s,t,u,v,z)

# 9
print('9.')
s = 'not a or b'
t = 'not (not b or c)'
u = 's and t'
v = 'not c or a'
z = 'u != v'
table(s,t,u,v,z)

# 10
print('10.')
s = 'a and b'
t = 'b and c'
u = 'not s or t'
v = 'c or not a'
z = 'not u or v'
table(s,t,u,v,z)

# 11
print('11.')
s = 'not (a != (not b))'
t = 'b and c'
u = 'not s or t'
v = '(not c) != (not a)'
z = 'not u or v'
table(s,t,u,v,z)

# 12
print('12.')
s = 'a or b'
t = 'not (b and c)'
u = 's != (not t)'
v = 'c or not a'
z = 'not u or v'
table(s,t,u,v,z)

# 13
print('13.')
s = 'not a or b'
t = 'b != c'
u = 's or t'
v = 'c or not a'
z = 'not u or v'
table(s,t,u,v,z)

# 14
print('14.')
s = 'a or not b'
t = 'not b or c'
u = 's and t'
v = 'not c or a'
z = 'u != v'
table(s,t,u,v,z)

# 15
print('15.')
s = 'not a or b'
t = 'not b or c'
u = 's or t'
v = 'c or not a'
z = 'not u or v'
table(s,t,u,v,z)

# 16
print('16.')
s = 'not a or b'
t = 'not b or c'
u = 's or t'
v = 'not c or not a'
z = 'not u or v'
table(s,t,u,v,z)

# 17
print('17.')
s = 'not a or not b'
t = 'b != c'
u = 's and t'
v = 'not (c or not a)'
z = 'not u or v'
table(s,t,u,v,z)

# 18
print('18.')
s = 'not a or b'
t = 'not (not b or c)'
u = 's or t'
v = 'not c or a'
z = 'u != v'
table(s,t,u,v,z)

# 19
print('19.')
s = 'a != b'
t = 'b or c'
u = 'not s or t'
v = '(not c) != (not a)'
z = 'not u or v'
table(s,t,u,v,z)

# 20
print('20.')
s = 'not a or not b'
t = 'not (not b or c)'
u = 's and t'
v = 'c or a'
z = 'not u or v'
table(s,t,u,v,z)

# 21
print('21.')
s = 'a or b'
t = 'not (b and c)'
u = 's or t'
v = 'c or not a'
z = 'not u or v'
table(s,t,u,v,z)

# 22
print('22.')
s = 'not a or not b'
t = 'not (not b or c)'
u = 's and t'
v = 'c and a'
z = 'not u or v'
table(s,t,u,v,z)

# 23
print('23.')
s = 'a or b'
t = 'b or c'
u = 'not s or t'
v = 'c or not a'
z = 'not u or v'
table(s,t,u,v,z)

# 24
print('24.')
s = 'not a or b'
t = 'not (not b or not c)'
u = 's and t'
v = '(not c) != (not a)'
z = 'not u or v'
table(s,t,u,v,z)
