def productNum( num , n ):
    if num < n:
	    return productNum(n, num)
    elif n != 0:
	    return (num + productNum(num, n - 1))
    else:
	    return 0



if __name__ == "__main__":
    
    num = 5
    n = 2
    result = productNum(num, n)
    print("Product of", n, "x", num,"is", result)