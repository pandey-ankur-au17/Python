def productNum(num):
    if num == 0:
	    return 0
    return (num + productNum(int(num - 1)))



if __name__ == "__main__":

    num = 5
    result = productNum(num)
    print("Sum of first n natural",num,"is", result)