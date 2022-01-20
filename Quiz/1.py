
def check(numbers):
    for number in numbers:
        if numbers.count(number)>1:
            return True

numbers = [1,2,3,4,5,6,7,8]

if(check(numbers)):
    print(f"Numbers:{numbers}\nNumbers are repeating.")
else:
    print(f"Numbers:{numbers}\nNumbers are not repeating.")