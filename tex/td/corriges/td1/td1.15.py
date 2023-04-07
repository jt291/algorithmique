# -*- coding: utf-8 -*-
 
"""
(0 < x) and (x < 3) :
    not ((0 < x) and (x < 3))
    (not (0 < x)) or (not (x < 3))
    (x <= 0) or (x >= 3)

(x < -2) or (x > 4) :
    not ((x < -2) or (x > 4))
    (not (x < -2)) and (not (x > 4))
    (x >= -2) and (x <= 4)
    
a and (not b) :
    not (a and (not b))
    (not a) or (not (not b))
    (not a) or b

(not a) or b :
    not ((not a) or b)
    (not (not a)) and (not b)
    a and (not b)
"""
