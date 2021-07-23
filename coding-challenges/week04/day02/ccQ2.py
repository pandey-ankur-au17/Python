# Accomplish the same task as Lists are US - 1 but without using the built-in
# extend() function of the list data type in python.
# Ex:
# Input 1:
# 1 2 3 4
# 11 434 1
# Output 1:
# 1 2 3 4 11 434 1
list1=[]
list2=[]
L=input("Enter the elements in list1 seprated by space:")
x=L.split()

for i in range(len(x)):
    x[i] = int(x[i])
list1.append(x)

L2=input("Enter the elements in list2 seprated by space:")
y=L2.split()

for i in range(len(y)):
    y[i] = int(y[i])
list2.append(y)

list3=list1+list2

print(list3)