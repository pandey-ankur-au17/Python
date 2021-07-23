# Given a decimal Number , Write a program to convert Decimal to Binary
# number.
# Input : 10 (decimal)
# Output: - 1010

def Decimal_to_Binary(number):
    binary = ""
    r=0
    while (number>0):
        r=number%2
        number=number//2
        binary = binary + str(r)
    print(binary[::-1])
    return binary[::-1]

number=int(input("Enter number to convert in to binary:"))
Decimal_to_Binary(number)
