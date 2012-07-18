import fileinput
import sys



mylist = []
for line in open('meta.txt','r').readlines():
    var = line.split()
    del var[0]
    del var[0]
    del mylist[:]
    var = ' '.join(var)
    stripped = open("stripped.txt",'a+')
    stripped.write(var)
    stripped.write("\n")
    
stripped.close()







def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

replaceAll("stripped.txt",'">','" />')


mylist = open("stripped.txt").readlines()

pilot = '<meta name="description" '+mylist[0]
pilot2 = '<meta name="DC.date.created" scheme="ISO8601" ' + mylist[1]
pilot3 = '<meta name="DC.date.modified" scheme="ISO8601" ' + mylist[2]


stripped = open("stripped.txt",'w')
stripped.write("\t")
stripped.write(pilot)
stripped.write("\t")
stripped.write(pilot2)
stripped.write("\t")
stripped.write(pilot3)
stripped.write("\n")
    
stripped.close()
