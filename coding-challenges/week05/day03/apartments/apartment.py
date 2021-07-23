class Apartment:
    def __init__(self):
        self.flats=[101,102,103,104]
        self.builder_name="Aloha Builder Group"
        self.amneties=["basket ball Play Ground","Cricket Ground","Swimming Pool","Club house","Gym"]
        self.parking_spots=20
        self.number_floors=[10]
        self.maintainance_monthly=3000
        self.has_elevator=True
        self.num_stairs=2
        self.fire_safety=True
        self.has_parking_permission=False
        self.current_renter=None
    def display_details(self):
        print(f"Builder Name is:",self.builder_name)

c=Apartment()