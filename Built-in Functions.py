import platform
import os
import datetime
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
inputText = input('Enter module/class name: ')
token = inputText.split(';')[-1]
if ( not os.path.exists('%s/built-ins/%s.txt'%(os.getcwd(),token))):    
    ims = "\n".join(inputText.split(';')[:-1])
    print('Executing: ',ims)
    exec(ims)

    code = ('dir(%s)' % token)
    l = eval(code)
    f = open(('built-ins/%s.txt' % (token)),'w')
    total = len(l)
    f.write('Python Version : %s\n\n'%(platform.python_version()))
    f.write("Built-in functions of '%s': \n\n" % (token))
    dashes = 0
    i = 1
    for s in l:
        if not(s.startswith('_')):
            f.write('%s\n'%('='*20))
            f.write('%02d ) %s\n'%(i,s))
            i += 1
        else:
            dashes += 1
    f.write('\n\n%s'%('*'*60))
    f.write('\nCopyright(c) Talha Asghar')
    f.write('\n%s'%('*'*60))
    f.close()
    print('Total: ',total)
    print('Real-Pythonic: ',dashes)
    print('Remaining: ' ,int(total)-int(dashes))

#os.startfile('%s/built-ins/%s.txt'%(os.getcwd(),token))
