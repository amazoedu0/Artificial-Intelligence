
def check(numbers):
    for number in numbers:
        if numbers.count(number)>1:
            return True

numbers = [(1,2,3,4,5,6,7,8),(1,2,3,4,5,6,6,7,8)]
for nums in numbers:
    if(check(nums)):
        print(f"Numbers:{nums}\nNumbers are repeating.")
    else:
        print(f"Numbers:{nums}\nNumbers are not repeating.")