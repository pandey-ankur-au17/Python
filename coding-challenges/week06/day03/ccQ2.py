# Given a number , find if the number is a perfect square root or not ?
# Also , find Time and space Complexity
# example :
# Input : n = 4
# output : - True
# Input : n = 10
# output : - False
import math
def find_perfect_square(N):
    if (N>=0):
        root=math.sqrt(N)
        return (root-math.floor(root)== 0)
    return False
N=int(input("Enter a Number to check Perfect Square:"))
if (find_perfect_square(N)):
    print("True")
else:
    print("False")


#Time complexity:-O(1)
#Space Complexity:-O(1)
