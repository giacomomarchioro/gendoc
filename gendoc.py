# -*- coding: utf-8 -*-
"""
Created on Mon May 30 16:38:49 2016
This module help you to write quickly docstring using variuous conventions
based on pep257 just copy the first line of the function and a wizard will guide
you.

The results will be prompt on the console.

@author: Giacomo Marchioro
"""
header = 'def histogram(self,vminx=None,vmaxx=None,auto=True,vlines=[]):'



def gendocnp(header):
    '''
    It prints the docstring of the function with a numpy style directly 
    to the console. I have added the default value.

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
    if header[-1]!=':':
        print "Function should end with colon"
        return
    args = header[:-2].split('(')[1].split(',')
    description = raw_input('Describe briefly what it does: ')
    argsdescritpion = []
    examples = {}    
    parent_class=None
    for i in args:
        if i == 'self':
            parent_class = raw_input('Wich is the parent class?')
            pass
        
        elif '=' in i:
            argsplitted = i.split('=')
            argdesc= raw_input('Descritpion of argument %s :  ' %(i) )
            typeinfo = raw_input('Type info: ')
            argsdescritpion.append("%s : %s \n \t %s (default %s)" %(argsplitted[0],typeinfo,argdesc,argsplitted[1]))
        else:
            argdesc= raw_input('Descritpion of argument %s : ' %(i))
            typeinfo = raw_input('Type info: ')
            argsdescritpion.append("%s : %s \n \t %s" %(i,typeinfo,argdesc))
    returns = raw_input('Describe briefly what it return: ')
    answer = raw_input('Do you want to write some example? (note function must be loaded) y/n ')
    if answer.lower() == 'y':        
        function_name = header[:-2].split('(')[0]
        if 'def' in function_name: #in case you placed the def or not
            function_name=function_name.split(' ')[1]
        go = True
        instance=None
        if parent_class!=None:
            instance = raw_input('specify the name of the instance, if you did not create an instance  /n you must create one before running this piece of code.' )
        while go:
            function_input= raw_input('Wirte only the input of the function ("!q" to finish) ')
            if function_input == '!q':
                break
            expression='%s(%s)' %(function_name,function_input)
            if instance==None:             
                examples[expression]=eval(expression)
            else:
                examples['self.%s' %(expression)]=eval("%s.%s" %(instance,expression))
    raises=[]          
    answer2 = raw_input('Do you want to write Rises section?  y/n ')
    if answer2.lower() == 'y':
        while go:
            raise_sentece= raw_input('Wirte the whole sentence ("!q" to finish) ')
            if raise_sentece == '!q':
                break
            raises.append(raise_sentece)
            
            
        
        
            
    #From here it starts to print 
    print'---------------------------------------'
    print'------------COPY FROM HERE ------------'
    print'---------------------------------------'
    if parent_class!=None:
        print 'Method of %s class' %(parent_class)
    print description
    print
    print"Parameters"
    print"----------"
    for i in argsdescritpion:
        print i
    print''
    print"Returns"
    print"-------"
    print returns
    print''
    if answer == 'y':
        print"Examples"
        print"--------"
        for i in examples:
            print ''
            print '>>> %s' %(i)
            print examples[i]
    if answer2 == 'y':
        print "Raises"
        print "------"
        for i in raises:
            print i

    
    
def gendocpep(header):
    '''Prints the docstring of the function following pep257 doc string
    convetion to the console.
    There is no much written there so the layout is minimalist.
    https://www.python.org/dev/peps/pep-0257/

    Keyword arguments:
    header -- Is the first line of the function. e.g. 'def test(a,b):'.
    
    Returns:
    It doesn't return anything it just print the docstring.
    
    Examples:
    >>> gendocnp('def test(a,b):')
        
    '''
    if header[-1]!=':':
        print "Function should end with colon"
        return
    args = header[:-2].split('(')[1].split(',')
    description = raw_input('Describe briefly what it does: ')
    argsdescritpion = []
    examples = {}    
    parent_class=None
    for i in args:
        if i == 'self':
            parent_class = raw_input('Wich is the parent class?')
            pass
        
        elif '=' in i:
            argsplitted = i.split('=')
            argdesc= raw_input('Descritpion of argument %s :  ' %(i) )
            argsdescritpion.append("%s -- %s  (default %s)" %(argsplitted[0],argdesc,argsplitted[1]))
        else:
            argdesc= raw_input('Descritpion of argument %s : ' %(i))
            argsdescritpion.append("%s -- %s" %(i,argdesc))
    returns = raw_input('Describe briefly what it return: ')
    answer = raw_input('Do you want to write some example? (note function must be loaded) y/n ')
    if answer.lower() == 'y':        
        function_name = header[:-2].split('(')[0]
        if 'def' in function_name: #in case you placed the def or not
            function_name=function_name.split(' ')[1]
        go = True
        instance=None
        if parent_class!=None:
            instance = raw_input('specify the name of the instance, if you did not create an instance  /n you must create one before running this piece of code.' )
        while go:
            function_input= raw_input('Wirte only the input of the function ("!q" to finish) ')
            if function_input == '!q':
                break
            expression='%s(%s)' %(function_name,function_input)
            if instance==None:             
                examples[expression]=eval(expression)
            else:
                examples['self.%s' %(expression)]=eval("%s.%s" %(instance,expression))
    
    raises=[]          
    answer2 = raw_input('Do you want to write Rises section?  y/n ')
    if answer2.lower() == 'y':
        print "Write something like this:"
        print "ValueError: If `param2` is equal to `param1`."
        go = True
        while go:
            raise_sentece= raw_input('Wirte the whole sentence ("!q" to finish) ')
            if raise_sentece == '!q':
                break
            raises.append(raise_sentece)
        
        
            
    #From here it starts to print 
    print'---------------------------------------'
    print'------------COPY FROM HERE ------------'
    print'---------------------------------------'
    if parent_class!=None:
        print 'Method of %s class' %(parent_class)
    print description
    print
    print"Keyword arguments:"
    for i in argsdescritpion:
        print i
    print''
    print"Returns:"
    print returns
    print''
    if answer == 'y':
        print"Examples:"
        for i in examples:
            print ''
            print '>>> %s' %(i)
            print examples[i]
            
    if answer2 == 'y':
        print "Raises"
        print "------"
        for i in raises:
            print i

def gendocgoogle(header):
    '''
    It prints a Google styled docsring of the procedure directl to the console.
    
    Args:
        header (str): Is the first line of the procedure. e.g. 'def test(a,b)'.
    
    Returns:
        It doesn't return anything it just print the docstring.
    
    Examples:

        >>> gendocnp('def test(a,b):')
        
    '''
    if header[-1]!=':':
        print "Function should end with colon"
        return
    args = header[:-2].split('(')[1].split(',')
    description = raw_input('Describe briefly what it does: ')
    argsdescritpion = []
    examples = {}    
    parent_class=None
    for i in args:
        if i == 'self':
            parent_class = raw_input('Wich is the parent class?')
            pass
        
        elif '=' in i:
            argsplitted = i.split('=')
            argdesc= raw_input('Descritpion of argument %s :  ' %(i) )
            typeinfo = raw_input('Type info: ')
            argsdescritpion.append("%s (%s): %s. Defaults to %s." %(argsplitted[0],typeinfo,argdesc,argsplitted[1]))
        else:
            argdesc= raw_input('Descritpion of argument %s : ' %(i))
            typeinfo = raw_input('Type info: ')
            argsdescritpion.append("%s (%s): %s." %(i,typeinfo,argdesc))
    returntype = raw_input('Describe briefly what the type of the output: ')
    if returntype!='':
        returntype += ': '
    returns = raw_input('Describe briefly what it returns: ')    
    answer = raw_input('Do you want to write some example? (note function must be loaded) y/n ')
    if answer.lower() == 'y':        
        function_name = header[:-2].split('(')[0]
        if 'def' in function_name: #in case you placed the def or not
            function_name=function_name.split(' ')[1]
        go = True
        instance=None
        if parent_class!=None:
            instance = raw_input('specify the name of the instance, if you did not create an instance  /n you must create one before running this piece of code.' )
        while go:
            function_input= raw_input('Wirte only the input of the function ("!q" to finish) ')
            if function_input == '!q':
                break
            expression='%s(%s)' %(function_name,function_input)
            if instance==None:             
                examples[expression]=eval(expression)
            else:
                examples['self.%s' %(expression)]=eval("%s.%s" %(instance,expression))
    
    raises=[]          
    answer2 = raw_input('Do you want to write Rises section?  y/n ')
    if answer2.lower() == 'y':
        go = True 
        while go:
            raise_sentece= raw_input('Wirte the whole sentence ("!q" to finish) ')
            if raise_sentece == '!q':
                break
            raises.append(raise_sentece) 
        
        
            
    #From here it starts to print 
    print'---------------------------------------'
    print'------------COPY FROM HERE ------------'
    print'---------------------------------------'
    if parent_class!=None:
        print 'Method of %s class' %(parent_class)
    print description
    print
    print"Args:"
    for i in argsdescritpion:
        print '\t'+i
    print''
    print"Returns:"
    print '\t'+returntype+returns
    print''
    if answer == 'y':
        print"Examples:"
        for i in examples:
            print ''
            print '\t >>> %s' %(i)
            print examples[i]

    if answer2 == 'y':
        print "Raises:"
        for i in raises:
            print '\t'+i