# Given an sorted integer array . Write a program to find Lower Bound of
# target number, return the index of the element
# Input: arr = [1,2 ,3,3,3,4,4,5,5,7,7,7] , target = 6
# Output: 8

def Lower_Bound(arr , target):
    prev=-1
    for i in range(0,len(arr)):
        if(target==arr[i]):
            print (i)
            return i
        elif (arr[i]>target):
            print(prev)
            return prev
        prev=i
Lower_Bound([1,2,3,3,3,4,4,5,5,7,7,7],6)


#Time Complexity=O(N)
#Space complexity=O(1)