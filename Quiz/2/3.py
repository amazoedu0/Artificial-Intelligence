numbers = [922,914,854]

def check(num):
    return num>4**4 and num%34==4%34

for num in numbers:
    print(f"{num} : {check(num)}")