# Given a Square Matrix of Dimension NXM , find all Non-Diagonal
# Elements which are prime Numbers .
# Input : [ [1,2,3] , [4,5,6] , [7,8,9] ]
# # Output: - 2 , 3 , 7
from array import*
def Matrix(a):
    
    if i!=j and a<=3:
            return a
    elif i!=j and a>3:
        for k in range(2,a):
            if a%k==0:
                break
            else:
                return a
                break


# take number of rows and columns as input
rows=int(input("Enter number of rows="))
columns=int(input("Enter number of columns="))

#initializing empty matrix
matrix=[]

# give numbers to the matrix as input
for i in range(rows):
    a=[]    
    for j in range(columns):
        a.append(int(input("input a number=")))
    matrix.append(a)



# problem
for i in range(rows):
    for j in range(columns):
        if Matrix(matrix[i][j])== None:
            continue
        else:
            print(matrix[i][j],end=",")
    print()
        