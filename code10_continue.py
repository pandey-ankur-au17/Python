# Using break/continue on a nested loops of days and weeks (which you
# take as user input), skip out on the even days of all odd weeks.

# taking user input both week and day.

x=int(input("Enter the Number of Weeks:"))
y=int(input("Enter the number of days:"))

#using for loop to print the week and days.

for week in range(1,x+1):
    for day in range(1,y+1):
        

#providing some conditional statement here.

        if week%2 == 1 and day%2==0:

#using continue to skip some particular value.

            continue

        print("Week-", week, " Day-", day)