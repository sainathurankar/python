def PushZerosAtLast(arr):
    count=0
    for i in arr:
        if i!=0:
            arr[count]= i
            count+=1
    while count < len(arr):
        arr[count]=0
        count+=1
        
if __name__ == "__main__":
    arr=list(map(int,input("Enter array elements: ").split())) #atleast one zero
    print("Before Pushing zeros to last: ",*arr)
    PushZerosAtLast(arr)
    print("After Pushing zeros at last: ",*arr)
