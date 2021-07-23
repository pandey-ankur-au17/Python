# Write a program to compute the power of a number.
# Input - x = 10 , y = 5 , calculate = (x^y)
# Output : - 100000
# Example -
# pow(n, 5) will give you n to the power 5. Use recursion in it.

# def pow(x,y):
#     z=x**y
#     print(z)
# x=int(input("Enter number:"))
# y=int(input("Enter Power:"))
# pow(x,y)
def power(N, P):
    if P == 0:
        return 1
    elif P == 1:
        return N
      
    else:
        return (N*power(N, P-1))

N = int(input("Enter number:"))
P = int(input("Enter Power:")) 
print(power(N, P))