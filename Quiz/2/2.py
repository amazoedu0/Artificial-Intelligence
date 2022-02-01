numbers = [
    [19, 19, 15, 5, 5, 5, 1, 2],
    [19, 15, 5, 7, 5, 5, 2],
    [11, 12, 14, 13, 14, 13, 15, 14]
]

def check(num):
    return num.count(num[4]) == 3 and len(num) == 8

for num in numbers:
    print(f"{num} : {check(num)}")
