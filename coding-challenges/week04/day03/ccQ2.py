# Write a function called MaxSeq() which can take any number of inputs from the
# user and returns the highest number in that sequence as the output.
# [You cannot use the inbuilt function max() of python]
# Ex:
# Input 1:
# 11 2 3 4
# Output 1:
# 11

def Maxseq():
    a=[]
    n=int(input("Enter number of elements:"))
    for i in range(1,n+1):
        b=int(input("Enter element:"))
        a.append(b)
    print(a)
    a.sort()
    print("maximum element is:",a[n-1])
Maxseq()
