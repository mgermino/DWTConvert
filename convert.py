f = open('shorebird.htm')
f1 = open('ranges.txt', 'a')
doIHaveToCopyTheLine=False
for line in f.readlines():
  if '<td rowspan="2" width="1"></td>' in line:
    doIHaveToCopyTheLine=True
  if doIHaveToCopyTheLine:
    f1.write(line)
f1.close()
f.close()

