def while_loop():
    n = int(input("Enter the line number: "))
    a = n-1
    for i in range(1,2*n):
        while i <= n:
            print("."*(n-i),end="")
            print(" "*(2*i-1),end="")
            print("."*(n-i))
            break
        while i > n:
            print("."*(i-n),end="")
            print(" "*(2*a-1), end="")
            print("."*(i-n))
            a-=1
            break

# uncomment below to check the code
while_loop()