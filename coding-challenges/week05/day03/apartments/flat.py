class Flat:
    def __init__(self):
        self.bed_room=[]
        self.bath_rooms=[]
        self.kitchen=[]
        self.owner_name=None
        self.current_renter=None
        self.has_parking_permission=False
    def Display_deytails(self):
        print(f"Flat is of :",{self.owner_name})
x=Flat()
