#Given a string, display only those characters which are present at an even index number.

str=input("Enter the String:")
for i in range(len(str)):
    if i%2==0:
        print(str[i])