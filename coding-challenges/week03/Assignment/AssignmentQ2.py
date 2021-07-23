# Write code for the following sequence by taking line number as user input.
# n = 3
#   1
#  121
# 12321
# n = 4
#    1
#   121
#  12321
# 1234321

def pattern_2(n):
    x=1
    y=n-1
    for i in range(1,n+1):
        k=0
        for j in range(1,y+1):
            print(" ",end="")
        for j in range(1,x+1):
           if(j<=i):
               k=k+1
           else:
                k=k-1
           print(k,end="")
        print()
        x=x+2
        y=y-1

n=int(input("Enter the line for pattern:"))

pattern_2(n)