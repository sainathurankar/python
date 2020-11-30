def check(arr1,arr2):
    if len(arr1)!=len(arr2):
        return 0

    b1=arr1[0]
    b2=arr2[0]
    
    for i in range(1,len(arr1)):
        b1^=arr1[i]
    for i in range(1,len(arr2)):
        b2^=arr2[i]

    if b1^b2==0:
        return 1
    else:
        return 0


if __name__ == "__main__":
    arr1=list(map(int,input("Enter Elements of array1: ").split()))
    arr2=list(map(int,input("Enter Elements of array2: ").split()))
    output=["not equal","equal"]
    print("Given arrays are "+output[check(arr1,arr2)])