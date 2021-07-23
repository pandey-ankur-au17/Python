class Closet:
    def __init__(self):
        self.length=6
        self.breadth=4
        self.height=7
        self.max_capacity=12
        self.items=["books","cloths","laptop","watches"]
    def display_detailss(self):
        print(f"closets capacity are:", {self.max_capacity})

# a=Closet()
# print("Closets Items Are:",a.items)

# def store_items(self):
#         n=input("Enter the items:").split()
#         self.items.append(n)
#         print(self.items)
#         return self.items
# store_items(a)

# def fetch_items(self):
#         print(self.items[0])
#         return self.items[0]
# fetch_items(a)