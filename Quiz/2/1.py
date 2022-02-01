numbers = [
    [19, 19, 15, 5, 3, 5, 5, 2],
    [19, 15, 15, 5, 3, 3, 5, 2],
    [19, 19, 5, 5, 5, 5, 5]
]

def check(num):
    return num.count(19) == 2 and num.count(5) >= 3

for num in numbers:
    print(f"{num} : {check(num)}")
