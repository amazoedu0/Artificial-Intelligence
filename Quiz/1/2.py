from itertools import permutations
lst = ['a','e','i','o', 'u']
l = list(permutations(lst, len(lst)))
string = ""
for item in l:
    for j in range(len(lst)):
        string += item[j]
    print(string)
    string = ""
