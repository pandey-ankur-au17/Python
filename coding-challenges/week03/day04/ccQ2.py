# Using break/continue on a nested loops of days and weeks (which you
# take as user input), encounter the scenario where we miss the first 2
# classes ever and still complete the syllabus one week before the end.

# taking user input both week and day.

x=int(input("Enter the Number of Weeks:"))
y=int(input("Enter the number of days:"))

#using for loop to print the week and days.

for i in range(1,x+1):
    for j in range(1,y+1):
        if j<3 and i ==1 :

#using continue to skip some particular value.

            continue
        print("Week-",i, " Day-",j)

    if i == x-1:
        break