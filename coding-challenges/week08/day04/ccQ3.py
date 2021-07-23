# Write a function to return sum of rows of a matrix as a list: (5 marks)
# Sample Input:
# This matrix :
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# Sample output
# should return,
# 10
# 26
# 42
# 58

def Row_addition():

    rows=int(input("Row:"))
    cols=int(input("Column:"))
    a=[]
    for i in range(rows):
        arr=list(map(int,input("Elements:").split()))
        a.append(arr)

    lis=[]
    for i in range(0, rows):  
        sum_Row = 0;  
        for j in range(0, cols):  
            sum_Row = sum_Row + a[i][j];
        lis.append(sum_Row)

    print(lis)

Row_addition()