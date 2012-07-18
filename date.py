namefile = 'energycenter.htm'

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
    pass

year = datelist[0]
day = datelist[2]
date = month + ' ' + day + ',' + ' ' + year
#print (date)


outfile = open('date.txt', 'w')
outfile.writelines(date)
outfile.close()
