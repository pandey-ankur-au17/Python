
def by_while_loop():
    for i in range(1,n+1):
        while i <= (n//2+1):
            for j in range(i, 0, -1):
                print(j, end='')
            print("")
            break
        while i > (n//2+1):
            for j in range(n//2,0,-1):
                print(j, end='')
            print("")
            break

# to check above code uncomment below line
n=int(input("Enter the line:"))

by_while_loop()
