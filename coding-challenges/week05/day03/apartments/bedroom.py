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
v=Bedrooms()
