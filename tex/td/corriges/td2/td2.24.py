# -*- coding: utf-8 -*-
 
from turtle import *
x0 = 0
y0 = 0
r = 10
n = 5
m = 10
for i in range(n) :
    up()
    y = y0 - 2*r*i
    x = x0 + r*(i%2)
    goto(x,y)
    for j in range(m) :
        down()
        circle(r)
        up()
        x = x + 2*r
        goto(x,y)
