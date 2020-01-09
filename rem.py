import os
f = open("sample_test.m4a",'rb')
para = f.readlines()
para1 = []
for line in para:
    for i in line:
        if(not i.isalnum()):
           line = line.replace(i,'')
    para1.append(line)

newf = open("temp.txt",'w')
newf.writelines(para1)
