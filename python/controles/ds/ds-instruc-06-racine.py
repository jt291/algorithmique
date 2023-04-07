# -*- coding: utf-8 -*-
 
a = 729
x = 1
z = a
y = 0
t = x
print(a,x,z,t,y)
while x <= a: x = x*4

print(a,x,z,t,y)
t = x
while x > 1:
  x = x//4
  t = t//2 - x
  if t <= z: 
    z = z - t
    t = t + x*2
  y = t//2
  print(a,x,z,t,y)

print(a,x,z,t,y)
