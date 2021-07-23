# Write a function that takes line number as input (with default value of 5) and prints the following pattern.
# n=3
# .....
# .. ..
# .   .
# .. ..
# .....
# n = 5
# .......
# ... ...
# ..   ..
#  .   .
# ..   ..
# ... ...
# .......

def for_loop():
    ln = 1
    n = int(input("Enter the line number: "))
    for ln in range(1, n+1):
        print("."*(n-ln),end="")
        print(" "*(2*ln-1),end="")
        print("."*(n-ln))
    
    for ln in range(n-1, 0, -1):
        print("."*(n-ln),end="")
        print(" "*(2*ln-1), end="")
        print("."*(n-ln))

# uncomment below to check the code
for_loop()