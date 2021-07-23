# Print prime numbers between 1 to N :
# using for loop :
# Also , find the Time and Space complexity
# Example : -
# Input : - N = 10
# output : - [2 , 3 , 5 , 7 ]

def prime_number(N):
    list1=[]
    for num in range(1,N):

        if num > 1:

            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                list1.append(num)

    print(list1)

N=int(input("Enter Number to check all the prime number in between:"))

prime_number(N)


#Time complexity:-O(N^2)
#Space complexity:-O(N)