

f = open('shorebird.htm')
for line in f:
    if '<meta name="description"' in line:
        line=line.strip()
        outfile = open('meta.txt', 'w')
        outfile.writelines(line)
    else:
        pass

outfile.close()

f = open('shorebird.htm')
for line in f:
    if '<meta name="date"' in line:
        line=line.strip()
        outfile = open('meta.txt', 'a')
        outfile.writelines("\n")
        outfile.writelines(line)
    else:
        pass

outfile.close()

f = open('shorebird.htm')
for line in f:
    if '<meta name="date.modified"' in line:
        line=line.strip()
        outfile = open('meta.txt', 'a')
        outfile.writelines("\n")
        outfile.writelines(line)
    else:
        pass

outfile.close()

f = open('shorebird.htm')
for line in f:
    if '<title>' in line:
        line=line.strip()
        outfile = open('meta2.txt', 'a')
        outfile.writelines(line)
        outfile.writelines("\n")
    else:
        pass

outfile.close()


f = open('shorebird.htm')
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


f = open('shorebird.htm')
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


