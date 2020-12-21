import time
start_time = time.time()

arr1=[2,4,5,6,7,9,10,13]
arr2=[2,3,4,5,6,7,8,9,11,15]
new=list(set(arr1+arr2))


for i in range(len(new)):
    flag=0
    for j in range(len(new)-i):
        if new[j]>new[j+1]:
            new[j],new[j+1]=new[j+1],new[j]
            flag=1
        if flag==0:
            break
print(new)
print("--- %s seconds ---" % (time.time() - start_time))