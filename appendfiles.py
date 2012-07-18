# append file2 data to file1 data
meta2list = []
fin = open("step1.txt", "r")
data2 = fin.read()
fin.close()
fout = open("THEPAGE.txt", "a")
fout.write(data2)


meta2list = open("meta2.txt").readlines()
fout.write("\n")
fout.write("\t")
fout.write(meta2list[2])


fin = open("step2.txt", "r")
data2 = fin.read()
fin.close()
fout = open("THEPAGE.txt", "a")
fout.write(data2)

fin = open("stripped.txt", "r")
data2 = fin.read()
fin.close()
fout = open("THEPAGE.txt", "a")
fout.write("\n")
fout.write(data2)


fin = open("step3.txt", "r")
data2 = fin.read()
fin.close()
fout = open("THEPAGE.txt", "a")
fout.write(data2)


fin = open("final2.txt", "r")
data2 = fin.read()
fin.close()
fout = open("THEPAGE.txt", "a")
fout.write(data2)


fin = open("step4.txt", "r")
data2 = fin.read()
fin.close()
fout = open("THEPAGE.txt", "a")
fout.write(data2)



fout.close()
