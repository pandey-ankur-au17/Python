def by_while_loop():    
    print("by using while loop ")
    n = int(input("Enter the number of lines : "))
    line = 1
    while (line <= n):
        print(" " * (n - line), end="")
        digit = 1
        while digit <= line:
            print(digit, end="")
            if line == digit:
                rev_digit = line-1
                while rev_digit >= 1:
                    print(rev_digit, end="")
                    rev_digit = rev_digit-1
            digit = digit+1
        print()
        line = line+1

by_while_loop()