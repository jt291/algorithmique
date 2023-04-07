# -*- coding: utf-8 -*-
 
from turtle import *
from math import *

#-----------------------------------------------------------------------
def motif(figure,quinconce,x0=0,y0=0,a=0,dx=20,dy=20,n=5,m=4) :
    assert quinconce in [0,1]
    # dessin du motif
    for j in range(m) :
        xl = x0 + quinconce*dx*(j%2)/2
        yl = y0 + j*dy
        # dessin d'une ligne de figures
        nf = n - (j%2)
        if quinconce == 1 : nf = n - (j%2)
        else : nf = n
        for i in range(nf) :
            x, y = xl + i*dx, yl
            # dessin d'une figure
            up()
            goto(x,y)
            setheading(a)
            down()
            # tracé de la figure
            figure(x,y,a,dx,dy)
            
#-----------------------------------------------------------------------
def f1(x,y,a,dx,dy):
    c, d = 3, dx/2
    for k in range(c) :
        forward(d)
        left(360/c)
    for k in range(c) :
        forward(d)
        right(360/c)
    return

def f2(x,y,a,dx,dy):
    c, d = 4, dx/2
    for k in range(c) :
         forward(d)
         left(360/c)
    up()
    goto(x+d/2,y-d/2)
    setheading(a+45)
    down()
    for k in range(c) :
         forward(d*sqrt(2))
         left(360/c)
    return

def f3(x,y,a,dx,dy):
    c, d = 3, dx/2
    setheading(a+30)
    for k in range(c) :
         forward(d)
         left(360/c)
    up()
    goto(x+d/sqrt(3),y)
    setheading(a+90)
    down()
    for k in range(c) :
         forward(d)
         left(360/c)
    return

def f4(x,y,a,dx,dy):
    c, d = 3, dx/2
    for k in range(c) :
        forward(d)
        left(360/c)
    setheading(a-60)
    circle(d/sqrt(3))
    return

def f5(x,y,a,dx,dy):
    c, d = 3, dx/2
    for n in range(6) :
        setheading(a+n*60)
        for k in range(c) :
            forward(d)
            left(360/c)
    return

def f6(x,y,a,dx,dy):
    c, d = 3, dx/2
    setheading(a+30)
    for k in range(c) :
         forward(d)
         left(360/c)
    up()
    goto(x+d/sqrt(3),y+d/2)
    setheading(a-30)
    down()
    for k in range(c) :
         forward(d)
         left(360/c)
    return

def f7(x,y,a,dx,dy):
    c, d = 3, dx/2
    for n in range(6) :
        setheading(a+30+n*60)
        for k in range(c) :
            forward(d)
            left(360/c)
    return

def f8(x,y,a,dx,dy):
    c, d = 3, dx/2
    for k in range(c) :
         forward(d)
         left(360/c)
    up()
    goto(x+d/2,y+d/sqrt(3))
    setheading(a+60)
    down()
    for k in range(c) :
         forward(d)
         left(360/c)
    return

def f9(x,y,a,dx,dy):
    c, d = 3, dx/2
    setheading(a+30)
    for k in range(c) :
        forward(d)
        left(360/c)
    setheading(a-90)
    for k in range(c) :
        forward(d)
        left(360/c)
    return

def f10(x,y,a,dx,dy):
    c, d = 4, dx/2
    for k in range(c) :
         forward(d)
         left(360/c)
    up()
    goto(x+d/2,y)
    setheading(a+45)
    down()
    for k in range(c) :
         forward(d/sqrt(2))
         left(360/c)
    return

def f11(x,y,a,dx,dy):
    c, d = 3, dx/2
    for k in range(c) :
         forward(d)
         left(360/c)
    up()
    goto(x,y+d/sqrt(3))
    down()
    for k in range(c) :
         forward(d)
         right(360/c)
    return

def f12(x,y,a,dx,dy):
    c, d = 3, dx/2
    for k in range(c) :
        forward(d)
        right(360/c)
    setheading(a-120)
    circle(d/sqrt(3))
    return

#-----------------------------------------------------------------------
for i in range(1,13) :
    motif(eval('f'+str(i)),0,-650+(i-1)*120,-50)
    motif(eval('f'+str(i)),1,-650+(i-1)*120,50)
