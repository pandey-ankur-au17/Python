# Given an sorted integer array . Write a program to find UPPER Bound of
# target number , return the index of the element .
# Input : - [1,2,2,2,3,3,5,5,5,6,6,8,9] , target = 7
# Output: - 12


def Upper_bound(arr,target):
    upper=-1
    for i in range(0,len(arr)):
        if(arr[i]==target):
            upper=i
    return upper
arr=[1,2,2,2,3,3,5,5,5,6,6,8,9]
target=7
next=Upper_bound(arr,target)
if next==-1:
    for i in range(0,len(arr)):
        if arr[i]>target:
            target=arr[i]
            break
    print(Upper_bound(arr,target))
else:
    print(next)

#time complexity:-O(N)
#space complexity:-O(1)