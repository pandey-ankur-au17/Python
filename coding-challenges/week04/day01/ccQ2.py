# Write a function fibonacci(n) which returns the nth fibonacci number. This
# should be calcuated using the while loop. The default value of n should be 10.

def fibonacci(n=10):
    n1=0
    n2=1
    count=0
    while count<n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count=count+1

#n=int(input("Enter the numbers:"))

fibonacci()
