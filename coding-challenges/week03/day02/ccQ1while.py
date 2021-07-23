# Given a number as input from the user, print all its odd multiples from 1 to 21 if the number is odd
# and all even multiples from 2 to 20 if the number is even.
# Use both for loop and while loop.

#Entering user input here

x=int(input("Enter the Number:"))

#checking conditions here and printing the output.

if x%2==0:
    i=2
    while i<=20:
        print(x,"*",i,"=",x*i)
        i=i+2
elif x%2!=0:
    i=1
    while i<=21:
        print(x,"*",i,"=",x*i)
        i=i+2
