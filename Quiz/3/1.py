l1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
l2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]

def rem(lst,col):
    for row in lst:
        row.pop(col-1)
    return lst
        
print(f"\nBefore : {l1} \nAfter : {rem(l1,1)}\n")
print(f"Before : {l2} \nAfter : {rem(l2,3)}\n")