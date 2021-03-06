# We have seen an iterative approach for binary search algorithm , write a
# recursive approach for that.


def binary_search(arr, low, high, x):

    if high >= low:
 
        mid = (high + low) // 2
 
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        return -1
arr = [8,9,10,11,23,24]
x = 10
result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print(str(result))
else:
    print("Element is not present in array")