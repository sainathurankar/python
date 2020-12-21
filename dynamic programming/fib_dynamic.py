import time
start_time = time.time()
def init(n):
    global lookup
    lookup=[None for i in range(n+1)]

def fib(n):
    if lookup[n]==None:
        if n<=1:
            lookup[n]=n
        else:
            lookup[n]=fib(n-1)+fib(n-2)
    return lookup[n]

n=int(input("Enter the number: "))
init(n)
print(fib(n))

print("--- Program executed in %s seconds ---" % (time.time() - start_time))