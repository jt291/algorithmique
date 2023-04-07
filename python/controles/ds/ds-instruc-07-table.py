# -*- coding: utf-8 -*-
 
for a in [0,1] :
    for b in [0,1] :
        for c in [0,1] :
            s7 = int(a and b and c)
            s6 = int(a and b and not c)
            s5 = int(a and not b and c)
            s4 = int(a and not b and not c)
            s3 = int(not a and b and c)
            s2 = int(not a and b and not c)
            s1 = int(not a and not b and c)
            s0 = int(not a and not b and not c)
            print(a,b,c,':',s0,s1,s2,s3,s4,s5,s6,s7)
