class Kitchen:
    def __init__(self):
        self.length=25
        self.breadth=30
        self.slab_material="Granite and wood"
        self.has_sink=True
        self.has_slab=True
        self.furnishing_materials="Plywood"
        self.lpg_pipeline=True
    def Display_deytails(self):
        print(f"Kitchen is of :",{self.slab_material})
x=Kitchen()