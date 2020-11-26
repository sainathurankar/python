#without yied i.e not generator
def range1(start,stop,ste=1):
    l=[]
    while start<stop:
        l.append(start)
        start+=ste
    return l

#generator function(it has yield)
def xrange1(start,stop,ste=1):
    while start<stop:
        yield start
        start+=ste
print(*range1(0,10,2)) #without using generator func


for i in xrange1(0,10,2):
    print(i,end=" ")   #using generator func