# Given an array arr[], find the maximum j – i such that arr[j] > arr[i] .
# Input :- arr = [ 34, 8, 10, 3, 2, 80, 30, 33, 1]
# Output : - 6 (j = 7, i = 1)
# Explanation : -
# Since at index ( j = 6 and i = 1 ) , we get maximum ( j - i ) where arr[j] > arr[i]
# Sample :
# Def find_max ( arr ):

list1=list(map(int,input("Enter the list=").split()))
max=0
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[j]>list1[i] and j-i>max:
                max=j-i

print(max)