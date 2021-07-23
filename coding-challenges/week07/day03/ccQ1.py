def Binarysearch(arr , target):
    low=0
    high=len(arr)+1
    mid=0 
    while low <= high:  
        mid = (high + low) // 2  
        if arr[mid] < target:  
            low = mid + 1    
        elif arr[mid] > target:  
            high = mid - 1  
        else:  
            return mid  
    return -1    
arr =[-1,0,3,5,9,12]
target =9
result = Binarysearch(arr,target)   
if result != -1:  
    print(str(result))  
else:  
    print("Element is not present in Array")


#    https://leetcode.com/problems/binary-search/submissions/