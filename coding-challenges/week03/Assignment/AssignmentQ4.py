# Write code for the following sequence by taking line number as user input, [using a single loop only]
# n = 5
# 1
# 21
# 321
# 21
# 1


n = int(input("Enter the number:"))
def by_for_loop():
    for i in range(1,n//2+1):
        for j in range(i, 0, -1):
            print(j, end='')
        print("")
        
    for i in range(n//2+1,0,-1):
        for j in range(i, 0, -1):
            print(j, end='')
        print("")

# to check above code uncomment below line
by_for_loop()
