# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

#taking input from user here.

x=int(input("Enter a number to print the pattern:"))

#logic to print the program.

for i in range(1,x+1):
    print(i*"*")

for i in range(x-1,0,-1):
    print(i*"*")