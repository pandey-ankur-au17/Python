# Given an array with NO Duplicates . Write a program to find PEAK
# ELEMENT
# Return value corresponding to the element of the peak element.
# Example :
# Input : - arr = [2,5,3,7,9,13,8]
# Output : - 5 or 13 (anyone)
# HINT : - Peak element is the element which is greater than both
# neighhbours.

def Peak_value(arr):
    s=arr.sort()
    for i in range(len(arr)):
        if arr[-1]>0:
            print(arr[-1])
            return arr[-1]
        elif arr[i] >arr [i-1] and arr[i] >arr[i+1]:
            print(arr[i])
            return arr[i]


arr = [2,5,3,7,9,13,8]

Peak_value(arr)