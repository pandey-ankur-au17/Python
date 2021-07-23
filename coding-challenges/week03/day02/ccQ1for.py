# Given a number as input from the user, print all its odd multiples from 1 to 21 if the number is odd
# and all even multiples from 2 to 20 if the number is even.
# Use both for loop and while loop.

#Entering user input here

x=int(input("Enter the Number:"))

#checking conditions here and printing the output.

if x%2==0:
    for i in range(2,21,2):
        print(x,"*",i,"=",x*i)
elif x%2!=0:
    for i in range(1,22,2):
        print(x,"*",i,"=",x*i)
