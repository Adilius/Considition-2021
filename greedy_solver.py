import operator


class GreedySolver:
    xp = 0
    zp = 0
    yp = 0

    light_packages = []
    medium_packages = []
    heavy_packages = []

    height_sorted_packages = []
    length_sorted_packages = []
    width_sorted_packages = []
    order_sorted_packages = []
    weight_sorted_packages = []

    placedPackages = []

    lastKnownMaxWidth = 0
    lastKnownMaxLength = 0
    lastKnownMaxHeight = 0

    def __init__(self, game_info):
        # Get vehicle information
        self.vehicle_length = game_info["vehicle"]["length"]
        self.vehicle_width = game_info["vehicle"]["width"]
        self.vehicle_height = game_info["vehicle"]["height"]

        # Add packages
        self.packages = game_info["dimensions"]
        for package in self.packages:

            # Add packages to lists
            self.height_sorted_packages.append({"height": package["height"], "id": package["id"]})
            self.length_sorted_packages.append({"length": package["length"], "id": package["id"]})
            self.width_sorted_packages.append({"width": package["width"], "id": package["id"]})
            self.order_sorted_packages.append({"order": package["orderClass"], "id": package["id"]})
            self.weight_sorted_packages.append({"weight": package["weightClass"], "id": package["id"]})

            if package["weightClass"] == 0:
                self.light_packages.append({"area": package["width"]*package["length"], "id": package["id"]})

            elif(package["weightClass"] == 1):
                self.medium_packages.append({"area": package["width"]*package["length"], "id": package["id"]})

            elif(package["weightClass"] == 2):
                self.medium_packages.append({"area": package["width"]*package["length"], "id": package["id"]})

        # Sort package lists
        self.height_sorted_packages = sorted(
            self.height_sorted_packages, key=lambda i: (i['height']))
        self.length_sorted_packages = sorted(
            self.length_sorted_packages, key=lambda i: (i['length']))
        self.width_sorted_packages = sorted(
            self.width_sorted_packages, key=lambda i: (i['width']))
        self.order_sorted_packages = sorted(
            self.order_sorted_packages, key=lambda i: (i['order']))
        self.weight_sorted_packages = sorted(
            self.weight_sorted_packages, key=lambda i: (i['weight']))

        #self.light_packages = sorted(
        #    self.light_packages, key=lambda i: (i['area']))
        #self.medium_packages = sorted(
        #    self.medium_packages, key=lambda i: (i['area']))
        #self.heavy_packages = sorted(
        #    self.heavy_packages, key=lambda i: (i['area']))

    def Solve(self):
        while len(self.packages) != 0:
            
            # Select a package
            #if self.zp <= self.lastKnownMaxHeight and len(self.weight_sorted_packages) != 0 :
            #    id = self.weight_sorted_packages.pop()["id"]
            #    package = self.packages[id]

            if len(self.heavy_packages) != 0 :
                id = self.heavy_packages[-1]["id"]
                for i in range(len(self.packages)):
                    if self.packages[i]["id"] == id:
                        package = self.packages[i]
                        break

            elif len(self.medium_packages) != 0 :
                id = self.medium_packages[-1]["id"]
                for i in range(len(self.packages)):
                    if self.packages[i]["id"] == id:
                        package = self.packages[i]
                        break

            elif len(self.light_packages) != 0:
                id = self.light_packages[-1]["id"]
                for i in range(len(self.packages)):
                    if self.packages[i]["id"] == id:
                        package = self.packages[i]
                        break

            if self.does_package_fit_all(package) == False:
                print("PACKAGE DOES NOT FIT")
                pass
        return self.placedPackages

    def SolveList(self, order = list):
        for package in order:
            self.AddPackage(str(package))
        return self.placedPackages

    def does_package_fit_all(self, package):
        # Check if it fits Z
        if self.DoesPackageFitZ(package):
            #print('z')
            self.AddPackage(package)
            self.zp += package["height"]

        # Check if it fits Y
        elif self.DoesPackageFitY(package):
            #print('y')
            self.yp += self.lastKnownMaxWidth
            self.zp = 0
            self.AddPackage(package)
            self.zp = package["height"]
            self.lastKnownMaxWidth = 0

        # Check if it fits X
        elif self.DoesPackageFitX(package):
            #print('x')
            self.xp += self.lastKnownMaxLength
            self.yp = 0
            self.zp = 0
            self.AddPackage(package)
            self.zp = package["height"]
            self.lastKnownMaxLength = 0

        else:
            print("Something went terribly wrong!")
            return 
        self.SetMaxX(package)
        self.SetMaxY(package)
        self.SetMaxZ(package)
        return 

    def DoesPackageFitX(self, package):
        return self.xp + self.lastKnownMaxLength + package["length"] < self.vehicle_length

    def DoesPackageFitY(self, package):
        return (self.yp + self.lastKnownMaxWidth + package["width"] < self.vehicle_width and
                self.xp + package["length"] < self.vehicle_length)

    def DoesPackageFitZ(self, package):
        return (self.xp + package["length"] < self.vehicle_length and
                self.yp + package["width"] < self.vehicle_width and
                self.zp + package["height"] < self.vehicle_height)

    def SetMaxY(self, package):
        if(package["width"] > self.lastKnownMaxWidth):
            self.lastKnownMaxWidth = package["width"]

    def SetMaxX(self, package):
        if(package["length"] > self.lastKnownMaxLength):
            self.lastKnownMaxLength = package["length"]

    def SetMaxZ(self, package):
        if(package["length"] > self.lastKnownMaxHeight):
            self.lastKnownMaxHeight = package["height"]

    def AddPackage(self, package):
        print("adding", package["id"])

        # Place it
        self.placedPackages.append(
            {
                "id": package["id"],
                "x1": self.xp, "x2": self.xp, "x3": self.xp, "x4": self.xp,
                "x5": self.xp + package["length"], "x6": self.xp + package["length"], "x7": self.xp + package["length"], "x8": self.xp + package["length"],
                "y1": self.yp, "y2": self.yp, "y3": self.yp, "y4": self.yp,
                "y5": self.yp + package["width"], "y6": self.yp + package["width"], "y7": self.yp + package["width"], "y8": self.yp + package["width"],
                "z1": self.zp, "z2": self.zp, "z3": self.zp, "z4": self.zp,
                "z5": self.zp + package["height"], "z6": self.zp + package["height"], "z7": self.zp + package["height"], "z8": self.zp + package["height"],
                "weightClass": package["weightClass"],
                "orderClass": package["orderClass"]
            }
        )

        # Remove it from lists
        self.height_sorted_packages[:] = [p for p in self.height_sorted_packages if p.get("id") != package["id"]]
        self.length_sorted_packages[:] = [p for p in self.length_sorted_packages if p.get("id") != package["id"]]
        self.width_sorted_packages[:] = [p for p in self.width_sorted_packages if p.get("id") != package["id"]]
        self.order_sorted_packages[:] = [p for p in self.order_sorted_packages if p.get("id") != package["id"]]
        self.weight_sorted_packages[:] = [p for p in self.weight_sorted_packages if p.get("id") != package["id"]]

        self.packages[:] = [p for p in self.packages if p.get("id") != package["id"]]

        self.light_packages[:] = [p for p in self.light_packages if p.get("id") != package["id"]]
        self.medium_packages[:] = [p for p in self.medium_packages if p.get("id") != package["id"]]
        self.heavy_packages[:] = [p for p in self.heavy_packages if p.get("id") != package["id"]]

