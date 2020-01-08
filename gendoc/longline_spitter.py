#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 13:08:28 2018

@author: opdate
"""



def add_PEPline(spaces, *tokens):
    '''
    Tab or spaces?
    Following PEP8 we can add spaces for formatting using the first argument
    avoid any tab
    https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces
    '''
    tobeprinted = []
    listo = [j for i in tokens for j in i.split(' ')]
    line = []
    if spaces != 0:
        line.append(" "*spaces)
    for i in listo:
        line.append(i)
        if len(" ".join(line)) > 79:
            tobeprinted.append(" ".join(line[:-1]))
            print line
            lastval = line[-1]
            line = []
            if spaces != 0:
                line.append(" "*spaces)
            line.append(lastval)
    if line != []:
        tobeprinted.append(" ".join(line))
    return tobeprinted
            
long_line = """Here you can get help of any object by pressing Ctrl+I in front of it, either on the Editor or the Console. Help can also be shown automatically after writing a left parenthesis next to an object. You can activate this behavior in Preferences > Help"""
word = "gsdlk xsdfsf"
funzia = " gasdm "
g = add_PEPline(4,long_line,word,funzia)
for i in g:
    print i 

     Here you can get help of any object by pressing Ctrl+I in front of it,
     either on the Editor or the Console. Help can also be shown automatically
     after writing a left parenthesis next to an object. You can activate this
     behavior in Preferences > Help gsdlk xsdfsf  gasdm