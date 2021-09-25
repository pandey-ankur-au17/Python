# n,m=list(map(int,input().split()))
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))

# outpt = [0]*len(b)
# i = 0
# j = 0
# while(i<len(a) and j < len(b)):
#     if(a[i]<b[j]):
#         outpt[j] = i+1
#         i += 1
#         continue
#     if(a[i] >= b[j]):
#         outpt[j] = i
#         j += 1

# while(len(a)<len(b) and j <len(b)):
#     outpt[j] = len(a)
#     j += 1
# for i in outpt:
#     print(i,end=" ")




# def uniq_string(string):
#     for char in string:
        
#         if string.count(char) > 1:
#             print("YES")
#         else:
#             print("NO")

# string=input()
# uniq_string(string)


# def half_division(A, n, count):
#     if count == 0:
#         return True
#     if n == 0 and count != 0:
#         return False
#     if A[n-1] > count:
#         return half_division(A, n-1, count)
 
#     return half_division(A, n-1, count) or half_division(A, n-1, count-A[n-1])
 
# def divion(A, n):
#     count = 0
#     for i in range(0, n):
#         count += A[i]
#     if count % 2 != 0:
#         return False
#     return half_division(A, n, count // 2)
# n=int(input())
# A = list(map(int,input().split()))
# if divion(A, n) == True:
#     print("YES")
# else:
#     print("NO")



# def half_partition(A, n):
#     count = 0
#     i, j = 0, 0
#     for i in range(n):
#         count += A[i]
 
#     if count % 2 != 0:
#         return False
 
#     div = [[True for i in range(n + 1)]
#             for j in range(count // 2 + 1)]
#     for i in range(0, n + 1):
#         div[0][i] = True
#     for i in range(1, count // 2 + 1):
#         div[i][0] = False
#     for i in range(1, count // 2 + 1):
 
#         for j in range(1, n + 1):
#             div[i][j] = div[i][j - 1]
 
#             if i >= A[j - 1]:
#                 div[i][j] = (div[i][j] or
#                               div[i - A[j - 1]][j - 1])
 
#     return div[count // 2][n]
# n=int(input())
# A = list(map(int,input().split()))
# if half_partition(A, n) == True:
#     print("YES")
# else:
#     print("NO")


