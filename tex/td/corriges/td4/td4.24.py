# -*- coding: utf-8 -*-
 
# chaîne -> code ASCII
def codeASCII(s):
    """"
    >>> codeASCII('bon')
    [98, 111, 110]
    """
    assert type(s) is str
    
    code = []
    for i in range(len(s)):
        code.append(ord(s[i]))
    return code

# Codes ASCII -> chaîne
def decodeASCII(code):
    """
    >>> decodeASCII([98, 111, 110])
    'bon'
    """
    assert type(code) is list
    
    s = ''
    for i in range(len(code)):
        s = s + chr(code[i])
    return s

#-----------------------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
