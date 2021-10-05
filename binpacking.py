import operator
from py3dbp import Packer, Bin, Item

class BinPacker:
    xp = 0
    zp = 0
    yp = 0
    placedPackages = []

    def __init__(self, game_info):
        self.packer = Packer()
        # Get vehicle information
        self.vehicle_length = game_info["vehicle"]["length"]
        self.vehicle_width = game_info["vehicle"]["width"]
        self.vehicle_height = game_info["vehicle"]["height"]

        self.packer.add_bin(Bin('',
        self.vehicle_length,
        self.vehicle_width,
        self.vehicle_height,99999))

        # Add packages
        self.packages = game_info["dimensions"]
        for package in self.packages:
            self.packer.add_item(Item(
                package["id"],
                package['length'],
                package['width'],
                package['height'],
                int(package['id'])))

        self.packer.pack(bigger_first=True ,distribute_items=False)

    def Solve(self):
        for b in self.packer.bins:
            print(":::::::::::", b.string())

        print("FITTED ITEMS:")
        for item in b.items:
            id = item.weight
            for i in range(len(self.packages)):
                    if self.packages[i]["id"] == id:
                        package = self.packages[i]
            self.AddPackage(package, int(float(item.position[0])), int(float(item.position[1])), int(float(item.position[2])), item.rotation_type)
            print("====> ", item.string())

        print("UNFITTED ITEMS:")
        for item in b.unfitted_items:
            print("====> ", item.string())

        print("***************************************************")
        print("***************************************************")
        return self.placedPackages
        
            


    def AddPackage(self, package, xp:int, yp:int, zp:int, rot:int):
        print("adding", package["id"])

        if rot == 0:
            # Place it
            self.placedPackages.append(
            {
                "id": package["id"],
                "x1": xp, "x2": xp, "x3": xp, "x4": xp,
                "x5": xp + package["length"], "x6": xp + package["length"], "x7": xp + package["length"], "x8": xp + package["length"],
                "y1": yp, "y2": yp, "y3": yp, "y4": yp,
                "y5": yp + package["width"], "y6": yp + package["width"], "y7": yp + package["width"], "y8": yp + package["width"],
                "z1": zp, "z2": zp, "z3": zp, "z4": zp,
                "z5": zp + package["height"], "z6": zp + package["height"], "z7": zp + package["height"], "z8": zp + package["height"],
                "weightClass": package["weightClass"],
                "orderClass": package["orderClass"]
            }
        )
        elif rot == 1:
            self.placedPackages.append(
            {
                "id": package["id"],
                "x1": xp, "x2": xp, "x3": xp, "x4": xp,
                "x5": xp + package["length"], "x6": xp + package["length"], "x7": xp + package["length"], "x8": xp + package["length"],
                "y1": yp, "y2": yp, "y3": yp, "y4": yp,
                "y5": yp + package["width"], "y6": yp + package["width"], "y7": yp + package["width"], "y8": yp + package["width"],
                "z1": zp, "z2": zp, "z3": zp, "z4": zp,
                "z5": zp + package["height"], "z6": zp + package["height"], "z7": zp + package["height"], "z8": zp + package["height"],
                "weightClass": package["weightClass"],
                "orderClass": package["orderClass"]
            }
        )
        elif rot == 2:
            self.placedPackages.append(
            {
                "id": package["id"],
                "x1": xp, "y1": yp, "z1": zp,
                "x2": xp, "y2": yp, "z2": zp,
                "x3": xp, "y3": yp, "z3": zp,
                "x4": xp, "y4": yp, "z4": zp,
                "x5": xp + package["width"], "y5": yp + package["height"], "z5": zp + package["length"],
                "x6": xp + package["width"], "y6": yp + package["height"], "z6": zp + package["length"], 
                "x7": xp + package["width"], "y7": yp + package["height"], "z7": zp + package["length"], 
                "x8": xp + package["width"], "y8": yp + package["height"], "z8": zp + package["length"],

                "weightClass": package["weightClass"],
                "orderClass": package["orderClass"]
            }
        )
        elif rot == 3:
            self.placedPackages.append(
            {
                "id": package["id"],
                "x1": xp, "x2": xp, "x3": xp, "x4": xp,
                "x5": xp + package["length"], "x6": xp + package["length"], "x7": xp + package["length"], "x8": xp + package["length"],
                "y1": yp, "y2": yp, "y3": yp, "y4": yp,
                "y5": yp + package["width"], "y6": yp + package["width"], "y7": yp + package["width"], "y8": yp + package["width"],
                "z1": zp, "z2": zp, "z3": zp, "z4": zp,
                "z5": zp + package["height"], "z6": zp + package["height"], "z7": zp + package["height"], "z8": zp + package["height"],
                "weightClass": package["weightClass"],
                "orderClass": package["orderClass"]
            }
        )
        elif rot == 4:
            self.placedPackages.append(
            {
                "id": package["id"],
                "x1": xp, "y1": xp, "z1": xp,
                "x2": xp, "y2": xp, "z2": xp,
                "x3": xp, "y3": xp, "z3": xp,
                "x4": xp, "y4": xp, "z4": xp,
                "x5": xp + package["length"], "y5": yp + package["width"], "z5": zp + package["height"],
                "x6": xp + package["length"], "y6": yp + package["width"], "z6": zp + package["height"], 
                "x7": xp + package["length"], "y7": yp + package["width"], "z7": zp + package["height"], 
                "x8": xp + package["length"], "y8": yp + package["width"], "z8": zp + package["height"],

                "weightClass": package["weightClass"],
                "orderClass": package["orderClass"]
            }
        )
        elif rot == 5:
            self.placedPackages.append(
            {
                "id": package["id"],
                "x1": xp, "y1": xp, "z1": xp,
                "x2": xp, "y2": xp, "z2": xp,
                "x3": xp, "y3": xp, "z3": xp,
                "x4": xp, "y4": xp, "z4": xp,
                "x5": xp + package["length"], "y5": yp + package["width"], "z5": zp + package["height"],
                "x6": xp + package["length"], "y6": yp + package["width"], "z6": zp + package["height"], 
                "x7": xp + package["length"], "y7": yp + package["width"], "z7": zp + package["height"], 
                "x8": xp + package["length"], "y8": yp + package["width"], "z8": zp + package["height"],

                "weightClass": package["weightClass"],
                "orderClass": package["orderClass"]
            }
        )

# Standard rotation      
""""
            self.placedPackages.append(
            {
                "id": package["id"],
                "x1": xp, "y1": xp, "z1": xp,
                "x2": xp, "y2": xp, "z2": xp,
                "x3": xp, "y3": xp, "z3": xp,
                "x4": xp, "y4": xp, "z4": xp,
                "x5": xp + package["length"], "y5": yp + package["width"], "z5": zp + package["height"],
                "x6": xp + package["length"], "y6": yp + package["width"], "z6": zp + package["height"], 
                "x7": xp + package["length"], "y7": yp + package["width"], "z7": zp + package["height"], 
                "x8": xp + package["length"], "y8": yp + package["width"], "z8": zp + package["height"],

                "weightClass": package["weightClass"],
                "orderClass": package["orderClass"]
            }
        )
""""