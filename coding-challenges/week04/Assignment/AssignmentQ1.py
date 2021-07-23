def print_rangoli(n):
    l1=list(map(chr,range(97,123)))
    x=l1[n-1::-1]+l1[1:n]
    m=len('-'.join(x))
    for i in range(1,n+1):
        print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(m,'-'))

n=int(input("Enter number to print Rangoli:"))
print_rangoli(n)