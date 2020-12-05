from itertools import permutations

n = int(input("Enter value of n: "))
List = [i for i in range(n)]
count=0
per = list(permutations(List))
for i in per:
    l=[1 if i[j]!=j else 0 for j in range(len(i)) ]
    if all(l):
        count+=1
print(count)