metalist = []
for line in open('meta.txt','r').readlines():
    var = line.split()
    var = ' '.join(var)
    metalist.append(var)
print (metalist)
