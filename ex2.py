def Partition(arr,s,e):
    pivot=arr[e]
    pIndex=s
    for i in range(s,e):
        if arr[i]<pivot:
            arr[i],arr[pIndex]=arr[pIndex],arr[i]
            pIndex+=1
    arr[e],arr[pIndex]=arr[pIndex],arr[e]
    return pIndex





def QuickSort(arr,s,e):
    if s<e:
        p=Partition(arr,s,e)
        QuickSort(arr,s,p-1)
        QuickSort(arr,p+1,e)




arr=list(map(int,input("Enter array elements: ").split()))
QuickSort(arr,0,len(arr)-1)
print("Sorted Array:",*arr)