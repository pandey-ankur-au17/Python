def listOperation():
    n=int(input("Enter the total step of operations:"))
    list1= []
    for i in range(n):
        step=input("Enter your step:")
        if(step=="insert"):
            v=int(input("Enter the value:"))
            p=int(input("Enter the position where you want to insert:"))
            list1.insert(p,v)
        elif step=="append":
            v=int(input("Enter the value:"))
            list1.append(v)
        elif step=="print":
            print(list1)
    return list1

print(listOperation())