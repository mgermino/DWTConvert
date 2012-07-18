import os

filenames = []

for filename in os.listdir('./convert'):
    filenames.append(filename)
filenames.remove('Done')
print (filenames)
