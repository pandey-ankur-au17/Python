# Write a Program to swap values , without using 3rd variable .
# Also find Time and Space Complexity ---
# Example : -
# Input : -
# A = 20 , B = 10
# Output : - A = 10 , B = 20

def swap(A,B):
    A=A+B
    B=A-B
    A=A-B
    print("Your swapped value are in A:",A)
    print("Your swapped value are in B:",B)
A=int(input("Enter first value to swap in A:"))
B=int(input("Enter second value to swap in B:"))
swap(A,B)

#time complexity:-O(1)
#space complexity:-O(1)