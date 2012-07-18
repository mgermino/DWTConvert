import sys
import os
import fileinput

filenames = []

for filename in os.listdir('./convert'):
    filenames.append(filename)
filenames.remove('Done')
filenames.remove('testfiles')

print ("These pages are being converted: )" + filenames

for x in filenames:
    namefile2 = []
    namefile = x
    namefile2 = namefile
    namefile = ('convert/' + namefile)
    endfile = 'convert/done/temporary.htm'

    f = open(namefile)
    for line in f:
        line=line.lower()
        outfile = open('extract.txt', 'a')
        outfile.writelines(line)
    else:
        pass

    outfile.close()
    f.close()



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
    replaceAll("final2.txt",'  ',' ')




    f = open('extract.txt')
    for line in f:
        if ('<meta name="description"') in line:
            line=line.strip()
            outfile = open('meta.txt', 'w')
            outfile.writelines("\t")
            outfile.writelines(line)
        else:
            pass

    outfile.close()

    f = open('extract.txt')
    for line in f:
        if '<meta name="date"' in line:
            line=line.strip()
            outfile = open('meta.txt', 'a')
            outfile.writelines("\n")
            outfile.writelines(line)
        else:
            pass

    outfile.close()

    f = open('extract.txt')
    for line in f:
        if '<meta name="date.modified"' in line:
            line=line.strip()
            outfile = open('meta.txt', 'a')
            outfile.writelines("\n")
            outfile.writelines(line)
        else:
            pass

    outfile.close()

    f = open(namefile)
    for line in f:
        if '<title>' in line:
            line=line.strip()
            outfile = open('meta2.txt', 'w')
            outfile.writelines(line)
            outfile.writelines("\n")
        else:
            pass

    outfile.close()


    f = open(namefile)
    for line in f:
        if '<p class="PageBranding">' in line:
            line=line.strip()
            line=line.strip('<p class="PageBranding">')
            line=line.strip('</p>')
            outfile = open('meta2.txt', 'a')
            outfile.writelines(line)
        else:
            pass

    outfile.close()


    f = open(namefile)
    for line in f:
        if '<h1>' in line:
            line=line.strip()
            line=line.strip('<h1>')
            line=line.strip('</h1>')
            outfile = open('meta2.txt', 'a')
            outfile.writelines("\n")
            outfile.writelines(line)
            outfile.writelines("\n")
        else:
            pass

    outfile.close()
    f.close()


    import fileinput
    import sys



    #mylist = []
    for line in open('meta.txt','r').readlines():
        var = line.split()
        del var[0]
        del var[0]
        #del mylist[:]
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

    pilot = '<meta '+mylist[0]
    pilot2 = '<meta name="DC.date.created" scheme="ISO8601" ' + mylist[1]
    pilot3 = '<meta name="DC.date.modified" scheme="ISO8601" ' + mylist[2]


    stripped = open("stripped.txt",'w')
    stripped.write(pilot)
    stripped.write("\t")
    stripped.write(pilot2)
    stripped.write("\t")
    stripped.write(pilot3)
    stripped.write("\n")
        
    stripped.close()


    # append file2 data to file1 data
    meta2list = []
    fin = open("header.txt", "r")
    data2 = fin.read()
    fin.close()
    fout = open(endfile, "w")
    fout.write(data2)


    meta2list = open("meta2.txt").readlines()
    fout.write("\n")
    fout.write("\t")
    fout.write(meta2list[0])


    fin = open("step1.txt", "r")
    data2 = fin.read()
    fin.close()
    fout = open(endfile, "a")
    fout.write(data2)

    fin = open("stripped.txt", "r")
    data2 = fin.read()
    fin.close()
    fout = open(endfile, "a")
    fout.write("\n")
    fout.write(data2)


    fin = open("step2.txt", "r")
    data2 = fin.read()
    fin.close()
    fout = open(endfile, "a")
    fout.write(data2)

    metalist2 = []
    metalist2 = open("meta2.txt").readlines()
    fout.write("\t\t\t\t")
    fout.write(metalist2[1])
    fout.write('\t\t\t\t</p><!-- #EndEditable -->\n')
    fout.write('\t\t\t\t<h1><!-- #BeginEditable "PageTitle" -->')
    fout.write(metalist2[2])
    fout.write('\t\t\t\t<!-- #EndEditable --></h1>\n')
    fout.write('\t\t\t\t<!-- #BeginEditable "MainContent" -->')
    

    fin = open("final2.txt", "r")
    data2 = fin.read()
    fin.close()
    fout = open(endfile, "a")
    fout.write(data2)
    

    fin = open("footer.txt", "r")
    data2 = fin.read()
    fin.close()
    fout = open(endfile, "a")
    fout.write(data2)



    fout.close()
    metalist2 = []
    metalist2 = open("meta2.txt").readlines()
    pagebranding = '\t\t\t\t' + metalist2[1] + '</p><!-- #EndEditable -->'



    f = open(namefile)
    datelist = []
    for line in f:
        if '<meta name="date.modified"' in line:
            datelist=line.split('"')
            datelist = datelist[3].split('-')

        else:
            pass


    if datelist[1] == '01':
        month = ("January")
    elif datelist[1] == '02':
        month = ("February")
    elif datelist[1] == '03':
        month = ("March")
    elif datelist[1] == '04':
        month = ("April")
    elif datelist[1] == '05':
        month = ("May")
    elif datelist[1] == '06':
        month = ("June")
    elif datelist[1] == '07':
        month = ("July")
    elif datelist[1] == '08':
        month = ("August")
    elif datelist[1] == '09':
        month = ("September")
    elif datelist[1] == '10':
        month = ("October")
    elif datelist[1] == '11':
        month = ("November")
    elif datelist[1] == '12':
        month = ("December")
    else:
        month = ("January")

    year = datelist[0]
    day = datelist[2]
    date = month + ' ' + day + ',' + ' ' + year
    f.close()

    replaceAll(endfile,'Month DD, YYYY',date)
    
    import shutil
    #cleanup
    os.remove('meta.txt')
    os.remove('meta2.txt')
    #os.remove('final2.txt')
    os.remove('stripped.txt')
    os.remove('extract.txt')


    filelist = []
    filelist = os.path.splitext(namefile)
    os.rename(namefile, filelist[0]+'_old.htm')

    os.rename(endfile, 'convert/done/' + namefile2)
