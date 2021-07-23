class Flat:
    def __init__(self):
        self.bed_room=25
        self.bath_rooms=30
        self.kitchen=30
        self.owner_name=None
        self.current_renter=None
    def Display_deytails(self):
        print(f"Flat is of :",{self.owner_name})
# x=Flat()
# def rent_out(self):
#     if self.current_renter==None:
#         self.carpet_area= 750
#         self.rent=5 * self.carpet_area
#         print("Your rent of this flat is:",self.rent)
#         self.ask_renter=input("You are ready to pay the amount typr Y or Yes or yes:")
#         if self.ask_renter=="Y" or "Yes" or "yes" or "y":
#             self.name=input("Enter your name:")
#             self.current_renter=self.name
#             print("current Renter is:",self.current_renter)
#         else:
#             print("Thank you for Visiting")
#     else:
#         print(self.current_renter)
# rent_out(x)


# def change_owner(self):
#     print("currently Owner of the flat is:",self.owner_name)
#     n=input("Enter the Name to change Owner:")
#     self.owner_name=n
#     print("new owner of the flat is:",self.owner_name)
# change_owner(x)