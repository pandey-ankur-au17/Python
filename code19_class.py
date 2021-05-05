class Beds:
    def __init__(self):
       self.length=6
       self.breadth=4
       self.year_made=2021
       self.has_headboard=True
       self.has_posts=True
       self.material="Steel and Wood"
    def display_details(self):
        print(f"Beds Specifications are:",{self.material})

x=Beds()
print("Beds Material are:",x.material)



#---------------------------------------------------------------------------------------------#

class Closet:
    def __init__(self):
        self.length=6
        self.breadth=4
        self.height=7
        self.max_capacity=12
        self.items=["books","cloths","laptop","watches"]
    def display_detailss(self):
        print(f"closets capacity are:", {self.max_capacity})

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

#------------------------------------------------------------------------------------#
class Bedrooms:
    def __init__(self):
        self.length=2000
        self.breadth=1200
        self.height=15
        self.beds=None
        self.closet=None
        self.has_balcony=True
        self.has_window=True
        self.num_lights=13
        self.has_ac=True
        self.has_fan=True
        self.charging_points=5
    def displaye_details(self):
        print(f"Bedrooms specifications are:", {self.height})
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
            print("bed Removed from the rooms:",self.beds)
remove_bed(v)

def remove_closet(self):
        if self.closet==None:
            print("No closet found in the room")
        elif self.closet != None:
            self.closet=None
            print("closet removed from the room:",self.closet)
remove_closet(v)
