import time

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

n=int(input("Enter the number: "))
start_time = time.time()
print(fib(n))

print("--- %s seconds ---" % (time.time() - start_time))