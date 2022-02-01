# numbers = [1,2,3,4,5,6,7,8,9,10]
# i=2
# print(f"List of numbers : {numbers}")
# leng=len(numbers)
# for _ in range(leng):
#     print(f"{numbers[i]} is removed from {numbers}")
#     # numbers.remove(numbers[i])
#     numbers.pop(i)
#     leng=len(numbers)
#     if leng<=i:
#         i-=1
# print(f"List at the End: {numbers}")
  
  
numbers = [1,2,3,4,5,6,7,8,9,10]
i=2
while numbers:
    if  i >= len(numbers) - 1:
        i -= len(numbers)
    elif len(numbers)<2:
        i=1
    print(numbers)
    print(f"{numbers.pop(i)} is removed")
    if len(numbers) < 2 and numbers:
        i=0
    else:
        i+=2
print(f"List at the End: {numbers}")
