# Q-2 ) Write a function that prints digits of a number from left to right , using
# recursion:(5 marks)
# Sample Input:
# 1234567
# Sample output:
# 1234567

def digit(num):
    if num < 10:
        print(num)
    else:
        digit(num // 10)
        print(num % 10)
num=int(input("Enter Number:"))
digit(num)