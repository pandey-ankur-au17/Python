class Solution:
    def getRow(rowIndex: int):
        tri=[[1], [1,1]]
        for i in range(2, rowIndex+1):
            row=[None]*(i+1)
            row[0]=1
            row[i]=1
            for j in range(1,i):
                row[j]=tri[i-1][j]+tri[i-1][j-1]
            tri.append(row)
        return tri[rowIndex]
    rowIndex=int(input("Enter:"))
    print(getRow(rowIndex))