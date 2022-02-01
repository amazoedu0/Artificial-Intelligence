import os
import dis
file = open('smstr7.txt', 'w')

names = ["Names","-"*40,"name1", "name2", "name3", "name4", "name5", "name6", "name7", "name8", "name9", "name10"]
qualities = ["Qualities","","quality1","quality2","quality3","quality4","quality5","quality6","quality7","quality8","quality9","quality10"]

file.write("-"*40+'\n')
for i in range(10):
    file.write(f"{names[i]:>15} {qualities[i]:>15}" + "\n")
    i+=1
file.write("-"*40+'\n')
