def arithmetic_operation(n=3, m=5, opname="+"):

    # provide input as Add  Sub Multiply And Divide for this operations

    if opname == "+":
        Sum = n + m
        print(Sum)
        return Sum
    elif opname == "-":
        Diff = n - m
        print(Diff)
        return Diff
    elif opname == "*":
        Mul = n * m
        print(Mul)
        return Mul
    elif opname == "/":
        Div = n / m
        print(Div)
        return Div


# providing hard input to perform operations
x = arithmetic_operation(3, 5, "+")
y = arithmetic_operation(-12, 23, "+")
print(x+y)


arithmetic_operation()
