import sys
import os
import fileinput
import re

fileObj = open('./convert/deep/nr029.htm', 'r')

pattern = "[A-z]+ [0-9][0-9], [0-9][0-9][0-9][0-9]"
prog=re.compile(pattern)
date = []

for line in fileObj:
    
    result==prog.search(line):
    print(line)
    else:
        pass


print (dir(line))


test = '<title>Tire Grants, April 19, 2000 Press Release</title>'
print(dir(test))
test.pattern
