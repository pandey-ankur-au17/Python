class Bathroom:
    def __init__(self):
        self.length=25
        self.breadth=30
        self.has_sink=True
        self.has_bathtub=True
        self.has_tap=True
        self.has_shower=True
    def Display_deytails(self):
        print(f"Bathroom is of :",{self.has_shower})
x=Bathroom()
