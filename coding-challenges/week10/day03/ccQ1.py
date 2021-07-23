def binToDecimal(bin):

    bitVal = 0
    i = 0
    while(bin != 0):

	    dec = bin % 10
	    bitVal = bitVal + dec * pow(2, i)
	    bin = bin // 10
	    i += 1

    print(bitVal)	
binToDecimal(101)