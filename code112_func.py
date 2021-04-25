# a. Define a function arithmetic_operation() which takes 2 numbers and operation name as input and performs an ope
# ration on them:
# * opname: "Add" - Then we add 2 numbers
# * opname: "Sub" - Then we subtract 2 numbers
# * opname: "Multiply" - Then we multiply 2 numbers
# * opname: "Divide" - Then we divide the 2 numbers
# Print the result of the operation and also return it.

def arithmatic_operation(n,m,opname):
    
#provide input as Add  Sub Multiply And Divide for this operations

    if opname == "Add":
        Sum = n + m
        print(Sum)
        return Sum
    elif opname == "Sub":
        Diff = n - m
        print(Diff)
        return Diff
    elif opname == "Multiply":
        Mul = n * m
        print(Mul)
        return Mul
    elif opname == "Divide":
        Div = n / m
        print(Div)
        return Div
#providing input for operations from user.

num1=int(input("input the number one:"))
num2=int(input("input the number one :"))

#Enter operation to perform.

opname=input("Enter operations Add, Sub, Multiply,Divide:")

#calling functions here.

arithmatic_operation(num1,num2,opname)
