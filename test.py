import BinarySearch
arr = list(map(int, input("Enter array elements: ").split()))
x = int(input("Enter element to search: "))

result = BinarySearch.binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
