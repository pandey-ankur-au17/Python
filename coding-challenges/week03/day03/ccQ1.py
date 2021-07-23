# Print the following pattern after taking in the line number as input from the user:
# for example: if input line number is 5, then print the following pattern.
#   *
#  ***
# *****
#  ***
#   *

#Taking input from user.

x=int(input("Enter a number to print the Diamond:"))

#Using for loop for iterations.

for i in range(1,x//2+2):
    print(" "*((x//2)-i+1)+"*"*(2*i-1))
for j in range(x//2+2,x+1):
    print(" "*(j-(x//2)-1)+"*"*(2*(x-j)+1))