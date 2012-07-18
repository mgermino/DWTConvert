import sys
import os
import fileinput

namefile = input("Enter file name: ")
#Removes all <td valign="top"> from file
inp = open(namefile,"r")
goodf = open("goodRanges.txt",'w+')
lines = inp.readlines()
for line in lines:
    if line.find('<td valign="top">') != -1:
        pass
    else:
        goodf.write(line)
   
goodf.close()
inp.close()

#Copies everything below <td rowspan="2" width="1"></td> and places into file
f = open('goodRanges.txt')
f1 = open('final.txt', 'a')
doIHaveToCopyTheLine=False
for line in f.readlines():
  if '<td rowspan="2" width="1"></td>' in line:
    doIHaveToCopyTheLine=True
  if doIHaveToCopyTheLine:
    f1.write(line)
f1.close()
f.close()
os.remove('goodRanges.txt')

#Searches <td rowspan="2" width="1"></td> and replaces with nothing
def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

replaceAll("final.txt",'<td rowspan="2" width="1"></td>',"")


# first, read everything from the old file
text = open("final.txt", 'rt').read()

# split it at the first empty line ("\n\n")
first, rest = text.split('<td valign="bottom">',1)

# make a new file and write the rest
open("final2.txt", 'wt').write(first)
os.remove('final.txt')
