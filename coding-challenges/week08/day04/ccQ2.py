# 2) Write a program to print sum of border elements of a square Matrix
# (5 marks)
# Border elements:
# 1 2 3 4
# 4 5 6 5
# 7 8 9 6
# 4 9 8 7
# Sum of border elements = 1+2+3+4+5+6+7+8+9+4+7+4 = 60

def Border_element(a, m, n):
    sum = 0
    for i in range(m):
        for j in range(n):
            if (i == 0):
                sum += a[i][j]
            elif (i == m-1):
                sum += a[i][j]
            elif (j == 0):
                sum += a[i][j]
            elif (j == n-1):
                sum += a[i][j]
    return sum

m=int(input("Row:"))
n=int(input("Column:"))
a=[]
for i in range(m):
    arr=list(map(int,input("Elements:").split()))
    a.append(arr)
total = Border_element(a, m, n)

print (total)