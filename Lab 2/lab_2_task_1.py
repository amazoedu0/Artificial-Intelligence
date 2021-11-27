def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fib(n-1)+fib(n-2))

n = int(input("\nEnter value of N for Fibonacci : "))
seq = list()
for i in range(1, n+1):
    seq.append(fib(i))

print(f"\nFor N = {n}  :  Sequence = {seq}\n")
