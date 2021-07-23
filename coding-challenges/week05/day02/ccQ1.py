from apartments.bed import Beds

x=Beds()
print("Beds Material are:",x.material)



from apartments.closet import Closet

a=Closet()
print("Closets Items Are:",a.items)

def store_items(self):
        n=input("Enter the items:").split()
        self.items.append(n)
        print(self.items)
        return self.items
store_items(a)

def fetch_items(self):
        print(self.items[0])
        return self.items[0]
fetch_items(a)


from apartments.bedroom import Bedrooms

v=Bedrooms()
print("Bedrooms Length:",v.length)
print("Bedrooms Breadth:",v.breadth)

def carpet_area(self):
        area=self.length*self.breadth
        print("Area of Bedrooms are:",area)
        return area
carpet_area(v)

def add_bed(self):
        bed=int(input("Enter bed:"))
        self.beds=bed
        print(self.beds)
add_bed(v)

def add_closet(self):
        closet=int(input("Enter closet:"))
        self.closet=closet
        print(self.closet)
add_closet(v)

def remove_bed(self):
        if self.beds==None:
            print("No bed found in the room")
        elif self.beds!=None:
            self.beds=None
            print("bed Removed from the rooms and value is:",self.beds)
remove_bed(v)

def remove_closet(self):
        if self.closet==None:
            print("No closet found in the room")
        elif self.closet != None:
            self.closet=None
            print("closet removed from the room and value is:",self.closet)
remove_closet(v)



from apartments.kitchen import Kitchen

x=Kitchen()

def cook(self):
    if self.lpg_pipeline==True and self.has_sink==True and self.has_slab==True:
        print("Kitchen can be used for cooking")
    else:
        print("unsuitable for cooking")
cook(x)




from apartments.bathroom import Bathroom

x=Bathroom()

def bathing(self):
    if self.has_tap==True or self.has_sink==True or self.has_shower==True:
        print("Suitable for bathing")
    else:
        print("unsuitable for Bathing")
bathing(x)




from apartments.flat import Flat

x=Flat()

def rent_out(self):
    if self.current_renter==None:
        self.carpet_area= 750
        self.rent=5 * self.carpet_area
        print("Your rent of this flat is:",self.rent)
        self.ask_renter=input("You are ready to pay the amount typr Y or Yes or yes:")
        if self.ask_renter=="Y" or "Yes" or "yes" or "y":
            self.name=input("Enter your name:")
            self.current_renter=self.name
            print("current Renter is:",self.current_renter)
        else:
            print("Thank you for Visiting")
    else:
        print(self.current_renter)
rent_out(x)


def change_owner(self):
    print("currently Owner of the flat is:",self.owner_name)
    n=input("Enter the Name to change Owner:")
    self.owner_name=n
    print("new owner of the flat is:",self.owner_name)
change_owner(x)