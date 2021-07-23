n= int(input("Enter the limit"))
def func(n):
    if n>=1:
        func(n-1)
        print("Time complexity")



#Time Complexity:-O(N)