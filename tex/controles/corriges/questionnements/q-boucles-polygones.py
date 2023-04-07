# -*- coding: utf-8 -*-
 
from turtle import *

#-----------------------------------------------------------------------
def motifPolygones(c,d,quinconce,x0=0,y0=0,a=0,dx=20,dy=20,n=5,m=4) :
    assert quinconce in [0,1]
    # dessin du motif
    for j in range(m) :
        xl = x0 + quinconce*dx*(j%2)/2
        yl = y0 + j*dy
        # dessin d'une ligne de figures
        if quinconce == 1 : nf = n - (j%2)
        else : nf = n
        for i in range(nf) :
            x, y = xl + i*dx, yl
            # dessin d'une figure
            up()
            goto(x,y)
            setheading(a)
            down()
            # tracé d'un polygone
            for i in range(c):
                 forward(d)
                 left(360/c)

#-----------------------------------------------------------------------
for i in range(3,11) :
    motifPolygones(i,10,0,-500+(i-3)*120,-50)
    motifPolygones(i,10,1,-500+(i-3)*120,50)
