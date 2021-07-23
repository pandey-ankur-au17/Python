#Using one for loop.

#Taking user input here.

x=int(input("Enter a number to print the Diamond:"))

#using one for loop to print the diamond.

for i in range(1,x+1):

  if i<=(x//2)+1:

    print(" "*((x//2)-i+1)+"*"*(2*i-1))

  else:

    print(" "*(i-(x//2)-1)+"*"*(2*(x-i)+1))