import os
file1=open('Lab 13/file1.txt','r')
file2=open('Lab 13/file2.txt','r')

tmp1=file2.readlines()
tmp2=file1.readlines()

file1.close()
file2.close()

file1=open('Lab 13/file1.txt','a')
file2=open('Lab 13/file2.txt','a')

file1.writelines(tmp1)
file2.writelines(tmp2)
