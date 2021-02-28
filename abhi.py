st = input()
l = list()
li=list()
for i in range(0,len(st),2):
    l.append(st[i:i+2])
for i in l:
    li.append(i[::-1])
print("".join(li))
