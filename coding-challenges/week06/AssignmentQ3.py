# Given an integer array , find all the numbers whose digit sum is even.
# Input : - [1 , 2 , 1111,56 ,22 ,89 ,100]
# Output: - [2 , 22 , 1111]
# Example : 2 -> digit sum = 2
# 22 -> digit sum = 4
# 1111 -> digit sum = 4

def Sum(number):
    sum=0
    while number!=0:
        a=number%10
        sum=sum+a
        number=number//10
    if sum%2==0:
        return 1

arr=list(map(int,input("Enter list of numbers=").split()))
a=[]
for i in arr:
    if Sum(i)==1:
        a.append(i)
print(a)

