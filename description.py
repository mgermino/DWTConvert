import re
import codecs


parsing =False
aList = []
TheList = []
headerlist = [] 
fileObj = codecs.open('./default.htm', 'r', "utf-8")
for line in fileObj:
    if line.find('<!DOCTYPE html') != -1:
        line
        parsing = True
    if line.find('"DocTitle" -->') != -1:
        parsing = False
        headerlist.append(line)

    
    if parsing:
        instruct = re.split(r"\s|," , line)
        aList.append(' '.join(instruct))
    else:
        pass
for x in aList:
    f = x.strip()
    TheList.append(f)


header1 = (' '.join(aList))
header2 = (''.join(headerlist))

header = (header1 + header2)
header = header.strip()

t = "\n"

outfile = codecs.open('headerTest.txt', 'wb', "utf-8")
for x in TheList:
    outfile.writelines(x + '\r\n')
    outfile.writelines(t)

outfile.writelines(header2)
outfile.close()


outfile1 = codecs.open('step1Test.txt', 'wb', "utf-8")
step1 = ['\t<!-- #EndEditable -->', '\t<meta http-equiv="content-type" content="text/html" />', '\t<meta http-equiv="Content-Style-Type" content="text/css" />', '\t<link rel="schema.DC" href="http://purl.org/dc/elements/1.1/" />', '\t<link rel="schema.DCTERMS" href="http://purl.org/dc/terms/" />', '\t<!-- #BeginEditable "RequiredMetas" -->']
for x in step1:
    outfile1.writelines(x + '\r\n')

outfile1.close()
fileObj.close()
#================================================================
parsing =False
aList = []
TheList = []
headerlist = [] 
fileObj = codecs.open('./default.htm', 'r', "utf-8")
for line in fileObj:
    if line.find('<!-- #BeginEditable "OptionalMetas" -->') != -1:
        line
        parsing = True
    if line.find('<!-- #BeginEditable "PageBranding" -->') != -1:
        parsing = False
        headerlist.append(line)

    
    if parsing:
        instruct = re.split(r"\s|," , line)
        aList.append(' '.join(instruct))
    else:
        pass
for x in aList:
    f = x.strip()
    TheList.append(f)


header1 = (' '.join(aList))
header2 = (''.join(headerlist))

header = (header1 + header2)
header = header.strip()

outfile = codecs.open('step2Test.txt', 'wb', "utf-8")
outfile.writelines('\t<!-- #EndEditable -->\r\n')
for x in TheList:
    outfile.writelines("\t" + x + '\r\n')
outfile.writelines('\t\t\t\t<!-- #BeginEditable "PageBranding" -->')
outfile.close()
fileObj.close()

#================================================================
parsing =False
aList = []
TheList = []
headerlist = [] 
fileObj = codecs.open('./default.htm', 'r', "utf-8")
for line in fileObj:
    if line.find('<div id="PageInfo">') != -1:
        line
        parsing = True
    if line.find('</html>') != -1:
        parsing = False
        headerlist.append(line)

    
    if parsing:
        instruct = re.split(r"\s|," , line)
        aList.append(' '.join(instruct))
    else:
        pass
for x in aList:
    f = re.sub('    ', "\t", x)
    g = re.sub('^ ', "\t", f)
    TheList.append(g)


header1 = (' '.join(aList))
header2 = (''.join(headerlist))

header = (header1 + header2)
header = header.strip()

outfile = codecs.open('footerTest.txt', 'wb', "utf-8")
outfile.writelines('\t\t\t<!-- #EndEditable -->\r\n')
for x in aList:
    outfile.writelines(x + '\r\n')
outfile.close()
fileObj.close()
