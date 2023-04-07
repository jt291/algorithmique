# -*- coding: utf-8 -*-
 
from turtle import *

def draw(n,d):
    assert type(n) is int
    assert n >= 0

    if n == 0: forward(d)
    else:
        draw(n-1,d/3.)
        left(60)
        draw(n-1,d/3.)
        right(120)
        draw(n-1,d/3.)
        left(60)
        draw(n-1,d/3.)
    return

up()
goto(0,-300)
setheading(0)
down()
draw(0,900)

up()
goto(0,-275)
setheading(0)
down()
draw(1,900)

up()
goto(0,-200)
setheading(0)
down()
draw(2,900)

up()
goto(0,-25)
setheading(0)
down()
draw(3,900)

up()
goto(0,150)
setheading(0)
down()
draw(4,900)
