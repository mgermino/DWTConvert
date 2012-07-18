import re
 
parsing =False
aList = []
descriplist = [] 
fileObj = open('./convert/energycenter.htm', 'r')
for line in fileObj:
    if line.find('<meta name="description"') != -1:
        print ("Now parsing **************************************")
        line
        parsing = True
    if line.find('.">') != -1:
        print ("Stopped parsing **********************************")
        parsing = False
        descriplist.append(line)
 
    if parsing:
        instruct = re.split(r"\s|," , line)
        aList.append(' '.join(instruct))
    else:
        pass

descrip1 = (' '.join(aList))
descrip2 = (''.join(descriplist[0]))

description = (descrip1 + descrip2)
