f = open("./convert/deep/legislation/fedleg.htm")
for line in f:
    if '<meta name="date.modified"' in line:
        modified = line
    else:
        pass

try:
    modified
except NameError:
    modified = 0



if modified == 0:
    print('<meta name="date.modified" content="1997-01-01">')
else:
    modified=modified.strip()
    print(modified)
