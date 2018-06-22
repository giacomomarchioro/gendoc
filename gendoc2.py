# -*- coding: utf-8 -*-
"""
Created on Mon May 30 16:38:49 2016
This module help you to write quickly docstring using variuous conventions
based on pep257 just copy the first line of the function and a wizard will guide
you.



The results will be prompt on the console.

@author: Giacomo Marchioro
"""
from __future__ import print_function
import clipboard
# This is for compatibility with Python 3.0 
# from builtins import input doesn't work
try:
    input = raw_input
except NameError:
    pass


header = 'def histogram(self,vminx=None,vmaxx=None,auto=True,vlines=[]):'

header2 = """def histogram(self,vminx=None,
            vmaxx=None,
            auto=True,
            vlines=[]):"""



def _get_args_list(header):
    ufargs = header[:-2].split('(')[1] #this takes the args part
    #removes \t and \n and white sapces
    return "".join(ufargs.split()).split(',')

def add_PEPline(spaces, *tokens):
    '''
    Lenght of the line?
    PEP-8 specify a maximum line length of 79 characters.
    Tab or spaces?
    Following PEP8 we can add spaces for formatting using the first argument
    avoid any tab.
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
            lastval = line[-1]
            line = []
            if spaces != 0:
                line.append(" "*spaces)
            line.append(lastval)
    if line != []:
        tobeprinted.append(" ".join(line))
    return tobeprinted

def _print_doc(tobeprinted):
    for i in tobeprinted:
        print (i)
   
def gendocnp(header=None,
             spaces=4,
             printoconsole = True,
             toclipper = True):
    '''
    It prints the docstring of the function with a numpy style directly 
    to the console. I have added the default value.
    https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt

    Parameters
    ----------
    header : str 
             Is the first line of the function. e.g. 'def test(a,b):'.
    
    Returns
    -------
    It doesn't return anything it just print the docstring.
    
    Examples
    --------
    >>> gendocnp('def test(a,b):')
        
    '''
    if header == None:
        header = clipboard.paste()
    if header[-1]!=':':
        print("Function should end with colon")
        return
    args = _get_args_list(header)
    examples = {}
    tobeprinted = []
    tobeprinted += add_PEPline(spaces,"\"\"\"")
    description = input('Describe briefly what it does:')
    tobeprinted += add_PEPline(spaces,description)
        
      
    #Parameters section:
    parent_class=None
    tobeprinted += add_PEPline(spaces,"")      
    tobeprinted += add_PEPline(spaces,"Parameters")
    tobeprinted += add_PEPline(spaces,"----------")
    for i in args:
        if i == 'self':
            parent_class = input('Wich is the parent class?')
            tobeprinted += add_PEPline(spaces,"Method of",parent_class," class")
        
        elif '=' in i:
            argsplitted = i.split('=')
            argdesc= input('Descritpion of argument %s :  ' %(i) )
            typeinfo = input('Type info: ')
            line =  "%s : %s" %(argsplitted[0],typeinfo)
            tobeprinted += add_PEPline(spaces,line)
            line2 =  "%s (default %s)" %(argdesc,argsplitted[1])
            tobeprinted += add_PEPline(spaces+4,line2)
            
        else:
            argdesc= input('Descritpion of argument %s : ' %(i))
            typeinfo = input('Type info: ')
            if typeinfo == '':
                line = i
            else:
                line = "%s : %s" %(i,typeinfo)
            tobeprinted += add_PEPline(spaces,line)
            tobeprinted += add_PEPline(spaces+4,argdesc)
    #Returns section:  
    tobeprinted += add_PEPline(spaces,"")      
    tobeprinted += add_PEPline(spaces,"Returns")
    tobeprinted += add_PEPline(spaces,"-------")
    returns = input('Describe briefly what it returns: ')
    tobeprinted += add_PEPline(spaces,returns)
    #Examples section:
    answer = input("""Do you want to write some example? 
                       (note function must be loaded) y/n """)
    tobeadded = []
    if answer.lower() == 'y':
        
        tobeadded += add_PEPline(spaces,"")      
        tobeadded += add_PEPline(spaces,"Examples")
        tobeadded += add_PEPline(spaces,"-------")        
        function_name = header[:-2].split('(')[0]
        if 'def' in function_name: #in case you placed the def or not
            function_name=function_name.split(' ')[1]
        go = True
        instance=None
        if parent_class != None:
            print("If you did if you did not create an instance")
            print(" you must create one before running this piece of code.") 
            instance = input('specify the name of the instance:')
        while go:
            text = 'Wirte only the arguments of the function ("!q" to finish) '
            function_input= input(text)
            if function_input == '!q':
                break
            expression='%s(%s)' %(function_name,function_input)
            if instance==None:             
                examples[expression]=eval(expression)
            else:
                command = "%s.%s" %(instance,expression)
                examples['self.%s' %(expression)]=eval(command)
    raises=[]          
    answer2 = input('Do you want to write Rises section?  y/n ')
    if answer2.lower() == 'y':
        tobeprinted += add_PEPline(spaces,"Rises")
        tobeprinted += add_PEPline(spaces,"-----")
        while go:
            text = 'Wirte the whole sentence ("!q" to finish) '
            raise_sentece= input(text)
            if raise_sentece == '!q':
                break
            raises.append(raise_sentece)
    tobeprinted += add_PEPline(spaces,"\"\"\"")
    
    if toclipper:
        clipboard.copy("\n".join(tobeprinted))
    if printoconsole:
        _print_doc(tobeprinted)
    return tobeprinted

#
#    
#def gendocpep(header):
#    '''Prints the docstring of the function following pep257 doc string
#    convetion to the console.
#    There is no much written there so the layout is minimalist.
#    https://www.python.org/dev/peps/pep-0257/
#
#    Keyword arguments:
#    header -- Is the first line of the function. e.g. 'def test(a,b):'.
#    
#    Returns:
#    It doesn't return anything it just print the docstring.
#    
#    Examples:
#    >>> gendocnp('def test(a,b):')
#        
#    '''
#    if header[-1]!=':':
#        print("Function should end with colon")
#        return
#    args = header[:-2].split('(')[1].split(',')
#    description = input('Describe briefly what it does: ')
#    argsdescritpion = []
#    examples = {}    
#    parent_class=None
#    for i in args:
#        if i == 'self':
#            parent_class = input('Wich is the parent class?')
#            pass
#        
#        elif '=' in i:
#            argsplitted = i.split('=')
#            argdesc= input('Descritpion of argument %s :  ' %(i) )
#            argsdescritpion.append("%s -- %s  (default %s)" %(argsplitted[0],
#                                   argdesc,
#                                   argsplitted[1]))
#        else:
#            argdesc= input('Descritpion of argument %s : ' %(i))
#            argsdescritpion.append("%s -- %s" %(i,argdesc))
#    returns = input('Describe briefly what it return: ')
#    answer = input("""Do you want to write some example? 
#                       (note function must be loaded) y/n """)
#    if answer.lower() == 'y':        
#        function_name = header[:-2].split('(')[0]
#        if 'def' in function_name: #in case you placed the def or not
#            function_name=function_name.split(' ')[1]
#        go = True
#        instance=None
#        if parent_class!=None:
#            instance = input('specify the name of the instance, if you did not create an instance  /n you must create one before running this piece of code.' )
#        while go:
#            function_input= input('Wirte only the input of the function ("!q" to finish) ')
#            if function_input == '!q':
#                break
#            expression='%s(%s)' %(function_name,function_input)
#            if instance==None:             
#                examples[expression]=eval(expression)
#            else:
#                examples['self.%s' %(expression)]=eval("%s.%s" %(instance,expression))
#    
#    raises=[]          
#    answer2 = input('Do you want to write Rises section?  y/n ')
#    if answer2.lower() == 'y':
#        print "Write something like this:"
#        print "ValueError: If `param2` is equal to `param1`."
#        go = True
#        while go:
#            raise_sentece= input('Wirte the whole sentence ("!q" to finish) ')
#            if raise_sentece == '!q':
#                break
#            raises.append(raise_sentece)
#        
#        
#            
#    #From here it starts to print 
#    print'---------------------------------------'
#    print'------------COPY FROM HERE ------------'
#    print'---------------------------------------'
#    if parent_class!=None:
#        print 'Method of %s class' %(parent_class)
#    print description
#    print
#    print"Keyword arguments:"
#    for i in argsdescritpion:
#        print i
#    print''
#    print"Returns:"
#    print returns
#    print''
#    if answer == 'y':
#        print"Examples:"
#        for i in examples:
#            print ''
#            print '>>> %s' %(i)
#            print examples[i]
#            
#    if answer2 == 'y':
#        print "Raises"
#        print "------"
#        for i in raises:
#            print i
#
#def gendocgoogle(header):
#    '''
#    It prints a Google styled docsring of the procedure directl to the console.
#    
#    Args:
#        header (str): Is the first line of the procedure. e.g. 'def test(a,b)'.
#    
#    Returns:
#        It doesn't return anything it just print the docstring.
#    
#    Examples:
#
#        >>> gendocnp('def test(a,b):')
#        
#    '''
#    if header[-1]!=':':
#        print "Function should end with colon"
#        return
#    args = header[:-2].split('(')[1].split(',')
#    description = input('Describe briefly what it does: ')
#    argsdescritpion = []
#    examples = {}    
#    parent_class=None
#    for i in args:
#        if i == 'self':
#            parent_class = input('Wich is the parent class?')
#            pass
#        
#        elif '=' in i:
#            argsplitted = i.split('=')
#            argdesc= input('Descritpion of argument %s :  ' %(i) )
#            typeinfo = input('Type info: ')
#            argsdescritpion.append("%s (%s): %s. Defaults to %s." %(argsplitted[0],typeinfo,argdesc,argsplitted[1]))
#        else:
#            argdesc= input('Descritpion of argument %s : ' %(i))
#            typeinfo = input('Type info: ')
#            argsdescritpion.append("%s (%s): %s." %(i,typeinfo,argdesc))
#    returntype = input('Describe briefly what the type of the output: ')
#    if returntype!='':
#        returntype += ': '
#    returns = input('Describe briefly what it returns: ')    
#    answer = input('Do you want to write some example? (note function must be loaded) y/n ')
#    if answer.lower() == 'y':        
#        function_name = header[:-2].split('(')[0]
#        if 'def' in function_name: #in case you placed the def or not
#            function_name=function_name.split(' ')[1]
#        go = True
#        instance=None
#        if parent_class!=None:
#            instance = input('specify the name of the instance, if you did not create an instance  /n you must create one before running this piece of code.' )
#        while go:
#            function_input= input('Wirte only the input of the function ("!q" to finish) ')
#            if function_input == '!q':
#                break
#            expression='%s(%s)' %(function_name,function_input)
#            if instance==None:             
#                examples[expression]=eval(expression)
#            else:
#                examples['self.%s' %(expression)]=eval("%s.%s" %(instance,expression))
#    
#    raises=[]          
#    answer2 = input('Do you want to write Rises section?  y/n ')
#    if answer2.lower() == 'y':
#        go = True 
#        while go:
#            raise_sentece= input('Wirte the whole sentence ("!q" to finish) ')
#            if raise_sentece == '!q':
#                break
#            raises.append(raise_sentece) 
#        
#        
#            
#    #From here it starts to print 
#    print'---------------------------------------'
#    print'------------COPY FROM HERE ------------'
#    print'---------------------------------------'
#    if parent_class!=None:
#        print 'Method of %s class' %(parent_class)
#    print description
#    print
#    print"Args:"
#    for i in argsdescritpion:
#        print '\t'+i
#    print''
#    print"Returns:"
#    print '\t'+returntype+returns
#    print''
#    if answer == 'y':
#        print"Examples:"
#        for i in examples:
#            print ''
#            print '\t >>> %s' %(i)
#            print examples[i]
#
#    if answer2 == 'y':
#        print "Raises:"
#        for i in raises:
#            print '\t'+i