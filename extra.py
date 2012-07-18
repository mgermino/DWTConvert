import sys
import os
import fileinput
import re
import codecs
from itertools import dropwhile
#removes </td>\n','</tr>\n','<tr>\n at end of all files
remove = ['</td>\n','</tr>\n','<tr>\n']
for x in remove:
    
    file = open("test.txt", 'r')
    dalist = []
    countlist = []
    count = 0
    for line in file:
        
        dalist.append(line)
        count += 1
        countlist.append(count)
        print("=============================================")


    darev = []
    countrev = []
    darev = dalist[::-1]
    countrev = countlist[::-1]
    darev = [x.strip(' ') for x in darev]


    def search(b):
     try:
      k=darev.index(x)
      return k+1

     except ValueError:
        return 0
    linenumber = (search(500))
    print(linenumber)

    linenumber = (search(500))
    x = "Not found"
    if linenumber != 0:
        origlinenum = countrev[linenumber]

        file.close()
        origlist = (countrev[linenumber])
        def mangle(fn):
            fo = open(fn, 'r')
            contents = fo.readlines()
            fo.close()
            contents[origlinenum] = contents[origlinenum].replace(dalist[origlist], '')
            fo = open(fn, 'w')
            fo.writelines(contents)
            fo.close()
        mangle('test.txt')
        print(dalist[origlist])
        

        
    else:
        print("fuck didnt work")



