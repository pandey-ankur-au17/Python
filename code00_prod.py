#Given two integer numbers return their product. If the product is greater than 1000, then return their sum
x=int(input())
y=int(input())

prod=x*y
if prod>1000:
    print(x+y)
else:
    print(prod)