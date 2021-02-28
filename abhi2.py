n = int(input())
arr = input().split()
l=list()
for i in arr:
    l.append(int(i))
l.sort()
print(l[-1]+l[-2])