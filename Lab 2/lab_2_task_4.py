import pandas as pn
from math import sqrt

def euclidian(list1,list2):
    distance=0
    for i in range(0,len(list1)):
        distance += (list1[i]-list2[i])**2
    return sqrt(distance) 

Series_1 = pn.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Series_2 = pn.Series([11, 8, 7, 5, 6, 5, 3, 4, 7, 1])

print(f"\nSeries 1:\n{Series_1.to_string(index=False)} \n\nSeries 2:\n \n{Series_2.to_string(index=False)}")

print(f"\nEuclidian Distance = {euclidian(Series_1,Series_2)}\n")
