# -*- coding: utf-8 -*-
 
from turtle import *

n, m = 5, 3
dx, dy = 30, 20
x0, y0 = 0, 0
for i in range(n+1):
    up()
    goto(x0+i*dx,y0)
    setheading(90)
    down()
    forward(m*dy)
for j in range(m+1):
    up()
    goto(x0,y0+j*dy)
    setheading(0)
    down()
    forward(n*dx)
