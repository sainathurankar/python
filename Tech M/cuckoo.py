def cuckoo(n):
    if n==0:
        return
    if n==1:
        return 0
    if n==2:
        return 1
    return 1*cuckoo(n-1)+2*cuckoo(n-2)+3

inp=int(input())
print(cuckoo(inp))