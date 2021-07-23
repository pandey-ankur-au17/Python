def sumOfDigits(num):
    if num == 0:
	    return 0
    return (num % 10 + sumOfDigits(int(num / 10)))



if __name__ == "__main__":

    num = 1234567
    result = sumOfDigits(num)
    print("Sum of digits in",num,"is", result)