#Take a number as input from the user, print its multiple of 2, 4, 6,
# 8, 10 if it is an odd number, if it is an even number then print its
# multiple of 1, 3, 5, 7 and 9.

#taking user input.

x=int(input("Enter the number:"))

#comparing if it is even or odd and printing.

if x%2 !=0:
    print(x,"* 2 =",x*2)
    print(x,"* 4 =",x*4)
    print(x,"* 6 =",x*6)
    print(x,"* 8 =",x*8)
    print(x,"* 10 =",x*10)
elif x%2==0:
    print(x,"* 1 =",x*1)
    print(x,"* 3 =",x*3)
    print(x,"* 5 =",x*5)
    print(x,"* 7 =",x*7)
    print(x,"* 9 =",x*9)