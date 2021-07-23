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
