# Take a name, age and whether user has diabetes as user input and tell
# them from when can they start taking vaccines for COVID-19. [Hint: you
# can refer to the news for the timelines for each age group]

#taking user input.

name=input("Enter your name:")
age=int(input("Ente your age:"))
diab=bool(input("Enter your Diabetic conditions in true and false:"))

if age>=18 and age<=35 and diab==True or diab==False:

    print("You are eligible for vaccination from 1 May")

elif age>=36 and age<=45 and diab==True or diab==False:

    print("You are eligible for vaccination form April go get your vaccine")

elif age>=46 and age<=100 and diab==True or diab==False:

    print("You are eligible for vaccination from March go get your vaccine immediately")

elif age>=101 and diab==True or diab==False:

    print("You Do not need vaccination Your time is up on Earth")