import os
with open("Lab 13/smstr7.txt", "r") as file:
    line = file.readline()
    while line:
        print(line,end="")
        line = file.readline()  