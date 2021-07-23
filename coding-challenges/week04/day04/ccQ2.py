Name= input("Enter Name seprated by space:").split()
Area=input("Enter address seprated by space:").split()
mob_N = input("Enter Mobile Numbers seprated by space:").split()

UserInput = {}

for idx in range(0,len(Name)):
      UserInput[(Name[idx]),Area[idx]] = mob_N[idx]


print(UserInput)