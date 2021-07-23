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

# x=Beds()
# print("Beds Material are:",x.material)