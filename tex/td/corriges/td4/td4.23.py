# -*- coding: utf-8 -*-
 
def f(t,debut,fin):
    m = (debut + fin)//2
    while m > 0:
        for i in range(m,fin+1):
            j = i - m
            while j >= debut:
                print(m,i,j,t)
                if t[j] > t[j+m]:
                    t[j],t[j+m] = t[j+m],t[j]
                    j = j - m
                else: j = debut-1
        m = m//2
    return t

t = [4,2,1,2,3,5]
print('avant :',t)
print('après :',f(t,0,5))
