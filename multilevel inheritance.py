class factory:
    def __init__(self, materials, zips):
        self.materials = materials
        self.zips = zips

class bhopalfactory(factory):
    def __init__(self, materials, zips, color):
        super().__init__(materials, zips)
        self.color = color

class punefactory(bhopalfactory):
    def __init__(self, materials, zips, color, pockets):
        super().__init__(materials, zips, color)
        self.pockets = pockets

# Creating object
obj = punefactory("leather", 2, "black", 3)

print(obj.materials)
print(obj.zips)
print(obj.color)
print(obj.pockets)