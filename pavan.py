inp=input("Enter a string : ").split()
l=[]
z=0
for i,a in enumerate("".join(inp)):
    l.append(a.upper()) if i%2==0 else l.append(a.lower())
for i in inp:
    print("".join(l[z:z+len(i)]),end=" ")
    z=z+len(i)
    














    
    
