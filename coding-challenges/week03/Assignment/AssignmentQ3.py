# Write code for the following sequence by taking line number as user input
# n = 3
#  1
# 121
#  1
# n = 5
#   1
#  121
# 12321
#  121
#   1

def by_for_loop():
    n= int(input ( "Enter the line="))
    for coloum in range(1,n//2 + n%2 +1):  #spaces
      print(" "*(n-coloum),end="")
      for rows in range(1,coloum+1):  
        print(rows,end="")
      for rows1 in range(coloum-1,0,-1):  
        print(rows1,end="")
      print()


    for coloum in range(n//2,0,-1): #spaces
      print(" "*(n-coloum),end="")
      for rows in range(1,coloum+1): 
        print(rows,end="")
      for rows1 in range(1,coloum):  
        print(rows1,end="")
      print() 

# uncomment below line to check code
by_for_loop()