# Write a function which takes a list as an input from the user [using the input()
# command] and returns the highest and the second highest elements of a list.
# Ex:
# Input 1:
# 1 2 3 4
# Output 1:
# 3 4

def Max_list():
    a=[]
    n=int(input("Enter number of elements:"))
    for i in range(1,n+1):
        b=int(input("Enter element:"))
        a.append(b)
    print(a)
    a.sort()
    print("Second Maximum Element is:",a[n-2])
    print("Maximum Element is:",a[n-1])
Max_list()