# -*- coding: utf-8 -*-
 
from turtle import *

n = 5
a = 50
x,y = 0,0
dx = 25
dy = -25
for j in range(n):
    up()
    x = x + dx
    y = y + dy
    goto(x,y)
    down()
    for i in range(3) :
        forward(a)
        left(120)
