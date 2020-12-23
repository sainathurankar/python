import time

def fib(n):
    f=[0,1]
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]

n=int(input("Enter the number: "))
start_time = time.time()
print(fib(n))

print("--- Program executed in %s seconds ---" % (time.time() - start_time))
