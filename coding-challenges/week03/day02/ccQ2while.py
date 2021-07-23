# Given a number as input from the user, print a triangle like the following.
# if input is 3:
# *
# **
# ***
# **
# *
# if input is 5:
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

#taking input from the user here 

x=int(input("Enter a number to print the pattern:"))

#logic of the program.

i=1
while x>=i:
    print(i*"*")
    i=i+1

i=1
while x>=i:
    print((x-1)*"*")
    x=x-1