# Given a sorted Integer array , Write a Program to search the target
# element using Binary Search, If target element is found return the index .
# Otherwise return -1 .
# Input : arr = [1,2,3,15,16,19,23,55,1000] , target = 15
# Output: - 3

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
arr = [1,2,3,15,16,19,23,55,1000]
target = 15
result = Binarysearch(arr,target)   
if result != -1:  
    print(str(result))  
else:  
    print("Element is not present in Array")  


#time complexity:-O(log N)
#space complexity:-O(1)