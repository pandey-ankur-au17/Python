class Bedrooms:
    def __init__(self):
        self.length=30
        self.breadth=25
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
# v=Bedrooms()
# print("Bedrooms Length:",v.length)
# print("Bedrooms Breadth:",v.breadth)

# def carpet_area(self):
#         area=self.length*self.breadth
#         print("Area of Bedrooms are:",area)
#         return area
# carpet_area(v)

# def add_bed(self):
#         bed=int(input("Enter bed:"))
#         self.beds=bed
#         print(self.beds)
# add_bed(v)

# def add_closet(self):
#         closet=int(input("Enter closet:"))
#         self.closet=closet
#         print(self.closet)
# add_closet(v)

# def remove_bed(self):
#         if self.beds==None:
#             print("No bed found in the room")
#         elif self.beds!=None:
#             self.beds=None
#             print("bed Removed from the rooms:",self.beds)
# remove_bed(v)

# def remove_closet(self):
#         if self.closet==None:
#             print("No closet found in the room")
#         elif self.closet != None:
#             self.closet=None
#             print("closet removed from the room:",self.closet)
# remove_closet(v)