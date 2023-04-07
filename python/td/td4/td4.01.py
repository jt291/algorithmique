# -*- coding: utf-8 -*-
 
from math import sqrt

def distance(m1,m2):
    assert type(m1) is tuple and len(m1) == 3
    assert type(m2) is tuple and len(m2) == 3
    (x1,y1,z1) = m1
    (x2,y2,z2) = m2
    d = (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) + (z2-z1)*(z2-z1)
    return sqrt(d)
