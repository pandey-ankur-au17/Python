# Given a integer array , find all the numbers which are palindrome:
# Note : -Palindromes are numbers when reversed will get the same as the
# original number.
# 121 - >palindrome , 123 → not a palindrome
# Input: [1 , 2 , 256 , 252 , 1441 , 969 ,2331]
# # Output: [1 , 2 , 252 , 1441 , 969 ]

#function
def Palindrome(a):
    length=len(a)
    first=0
    last=length-1
    while(first<last):
        if (a[first]==a[last]):
            first=first+1
            last=last=1
        else:
            return f"Not Palindrome"
    return f"Palindrome"



# take number of rows and columns as input
rows=int(input("Enter number elements="))


#initializing empty matrix
matrix=[]

# give numbers to the matrix as input
for i in range(rows):
        matrix.append(input("input a number="))



#problem logic 
a=[]
for i in matrix:
    if Palindrome(i)=="Palindrome":
        a.append(i)
    else:
        continue
print(a)
