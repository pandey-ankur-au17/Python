# - 1) Write a program to print sum of right diagonal of a matrix: (5 marks)
# Right diagonal is shown below:
# 1 2 3
# 4 5 6
# 7 8 9

def Right_diagonal(a,m,n):
    sum_right=0
    for i in range(m):
        for j in range(n):
            if i+j==n-1:
                sum_right=sum_right+a[i][j]
    
    return sum_right

m=int(input("Row:"))
n=int(input("Column:"))
a=[]
for i in range(m):
    arr=list(map(int,input("Elements:").split()))
    a.append(arr)

print(Right_diagonal(a,m,n))