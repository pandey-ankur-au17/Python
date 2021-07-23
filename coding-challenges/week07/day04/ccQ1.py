# Given a sorted array with Duplicates . Write a program to find LOWER
# BOUND of a TARGET using Binary search Method .
# Return Index corresponding the element of lower bound element.
# Example :
# Input : - arr = [1,1,1,2,2,3,3,4,5,5,5,7,7] , Target = 4
# Output : - 7

def Lower_bound(arr,target):
    n=len(arr)
    left=0
    right=n-1
    res=-1
    while(left<=right):
        mid=(left+right)//2
        if(arr[mid]==target):
            res=mid
            right=mid-1
        elif (arr[mid]>target):
            right=mid-1
        else:
            left=mid+1
    return res
arr=[1,1,1,2,2,3,3,4,5,5,5,7,7]
target=4
print(Lower_bound(arr,target))
