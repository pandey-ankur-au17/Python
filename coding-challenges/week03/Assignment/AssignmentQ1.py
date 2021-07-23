# 1. Write code for the following sequence by taking line number as user input:
# n = 5
# **
#  **
#   **
#  **
# **
# n=3
# **
#  **
# **

def pattern_1(n):
    for i in range(1,n+1):
        if i<=n//2+1:
            for k in range(1,i):
                print(" ",end="")
            for l in range(2):
                print("*",end="")
            print("\n")
        else:
            for m in range(n-i):
                print(" ",end="")
            for j in range(2):
                print("*",end="")
            print("\n")

n=int(input("Enter the line number:"))

pattern_1(n)