# -*- coding: utf-8 -*-
 
# s.capitalize()
s = 'bOnJoUr'
print('"',s,'".capitalize() -> "',s.capitalize(),'"',sep='')

# s.count(sub[,start[,end]])
s = 'bonjour'
sub, start, end = 'o', 0, len(s)
print('"',s,'".count("',sub,'",',start,',',end,') -> ',s.count(sub,start,end),sep='')

# s.endswith(suffix[,start[,end]])
s = 'bonjour'
suffix, start, end = 'jour', 0, len(s)
print('"',s,'".endswith("',suffix,'",',start,',',end,') -> "',s.endswith(suffix,start,end),'"',sep='')

# s.expandtabs([tabsize])
s = 'bonjour\t\tMonsieur'
tabsize = 1
print('"',s,'".expandtabs(',tabsize,') -> ',s.expandtabs(tabsize),sep='')

# s.find(sub[,start[,end]])/rfind(sub[,start[,end]])
s = 'bonjour'
sub, start, end = 'o', 0, len(s)
print('"',s,'".find("',sub,'",',start,',',end,') -> ',s.find(sub,start,end),sep='')
print('"',s,'".rfind("',sub,'",',start,',',end,') -> ',s.rfind(sub,start,end),sep='')

# s.index(sub[,start[,end]])/rindex(sub[,start[,end]])
s = 'bonjour'
sub, start, end = 'o', 0, len(s)
print('"',s,'".index("',sub,'",',start,',',end,') -> ',s.index(sub,start,end),sep='')
print('"',s,'".rindex("',sub,'",',start,',',end,') -> ',s.rindex(sub,start,end),sep='')

# s.isalnum()
s = 'bonjour2fois'
print('"',s,'".isalnum() -> ',s.isalnum(),sep='')

# s.isalpha()
s = 'bonjour2fois'
print('"',s,'".isalpha() -> ',s.isalpha(),sep='')

# s.isdigit()
s = '2175'
print('"',s,'".isdigit() -> ',s.isdigit(),sep='')

# s.isspace()
s ='\t \t\n'
print('"',s,'".isspace() -> ',s.isspace(),sep='')

# s.istitle()
s = 'Bonjour'
print('"',s,'".istitle() -> ',s.istitle(),sep='')

# s.islower()
s = 'bonjour'
print('"',s,'".islower() -> ',s.islower(),sep='')

# s.isupper()
s = 'BONJOUR'
print('"',s,'".isupper() -> ',s.isupper(),sep='')

# s.join(seq)
s = ''
seq = ['bon','j','our']
print('"',s,'".join(',seq,') -> "',s.join(seq),'"',sep='')

# s.ljust(width[,fillChar=' '])/rjust(width[,fillChar=' '])/center(width[,fillChar=' '])
s = 'bonjour'
width, fillChar = 14, '-'
print('"',s,'".ljust(',width,',"',fillChar,'") -> "',s.ljust(width,fillChar),'"',sep='')
print('"',s,'".rjust(',width,',"',fillChar,'") -> "',s.rjust(width,fillChar),'"',sep='')
print('"',s,'".center(',width,',"',fillChar,'") -> "',s.center(width,fillChar),'"',sep='')

# s.lower()/title()/upper()
s = 'BonJouR'
print('"',s,'".lower() -> "',s.lower(),'"',sep='')
print('"',s,'".title() -> "',s.title(),'"',sep='')
print('"',s,'".upper() -> "',s.upper(),'"',sep='')

# s.lstrip([chars])/rstrip([chars])/strip([chars])
s = 'bonjour'
chars = 'nob'
print('"',s,'".lstrip("',chars,'") -> "',s.lstrip(chars),'"',sep='')
chars = 'ru'
print('"',s,'".rstrip("',chars,'") -> "',s.rstrip(chars),'"',sep='')
chars = 'orb'
print('"',s,'".strip("',chars,'") -> "',s.strip(chars),'"',sep='')

# s.partition(separ)/rpartition(separ)
s = 'bonjour'
separ = 'o'
print('"',s,'".partition("',separ,'") -> ',s.partition(separ),sep='')
print('"',s,'".rpartition("',separ,'") -> ',s.rpartition(separ),sep='')

# s.replace(old,new[,maxCount=-1])
s = 'bonjour'
old, new, maxCount = 'o', 'O', 1
print('"',s,'.replace("',old,'",',new,'",',maxCount,') -> ',s.replace(old,new,maxCount),sep='')

# s.split([separ[,maxsplit]])/rsplit([separ[,maxsplit]])
s = 'bonjour'
separ, maxsplit = 'o', 1
print('"',s,'.split("',separ,'",',maxsplit,') -> ',s.split(separ,maxsplit),sep='')
print('"',s,'.rsplit("',separ,'",',maxsplit,') -> ',s.rsplit(separ,maxsplit),sep='')

# s.splitlines([keepends])
s = 'bonjour\nça va ?\nmerci\n'
keepends = True
print('"',s,'".splitlines(',keepends,') -> ',s.splitlines(keepends),sep='')
keepends = False
print('"',s,'".splitlines(',keepends,') -> ',s.splitlines(keepends),sep='')

# s.startswith(prefix[,start[,end]])
s = 'bonjour'
prefix, start, end = 'bo', 0, len(s)
print('"',s,'".startswith("',prefix,'",',start,',',end,') -> ',s.startswith(prefix,start,end),sep='')

# s.swapcase()
s = 'bonjour'
print('"',s,'".swapcase() -> "',s.swapcase(),'"',sep='')

# s.zfill(width)
s = '-3.14'
width = 14
print('"',s,'".zfill(',width,') -> "',s.zfill(width),'"',sep='')
