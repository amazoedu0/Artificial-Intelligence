lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def rotate(lst,move,steps):
    if move=='left':
        return lst[steps:]+lst[:steps]
    elif move=='right':
        return lst[-steps:]+lst[:-steps]

print(f"\nList : {lst} \nLeft Rotate by 4  :  {rotate(lst,'left',4)}\n")
print(f"\nList : {lst} \nLeft Rotate by 2  :  {rotate(lst,'left',2)}\n")
print(f"\nList : {lst} \nRight Rotate by 4 :  {rotate(lst,'right',4)}\n")
print(f"\nList : {lst} \nRight Rotate by 2 :  {rotate(lst,'right',2)}\n")