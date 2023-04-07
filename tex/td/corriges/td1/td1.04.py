# -*- coding: utf-8 -*-
 
from math import log, ceil

# 1 ko (kilooctet)
k = 3
x = ceil(k*log(10)/log(2))
print(k,x,10**k,2**x)

# 1 Mo (mégaoctet)
k = 6
x = ceil(k*log(10)/log(2))
print(k,x,10**k,2**x)

# 1 Go (gigaoctet)
k = 9
x = ceil(k*log(10)/log(2))
print(k,x,10**k,2**x)

# 1 To (téraoctet)
k = 12
x = ceil(k*log(10)/log(2))
print(k,x,10**k,2**x)

# 1 Po (pétaoctet)
k = 15
x = ceil(k*log(10)/log(2))
print(k,x,10**k,2**x)

# 1 Eo (exaoctet)
k = 18
x = ceil(k*log(10)/log(2))
print(k,x,10**k,2**x)

# 1 Zo (zettaoctet)
k = 21
x = ceil(k*log(10)/log(2))
print(k,x,10**k,2**x)

# 1 Yo (yottaoctet)
k = 24
x = ceil(k*log(10)/log(2))
print(k,x,10**k,2**x)
