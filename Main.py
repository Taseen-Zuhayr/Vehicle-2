class vehicle:
    def __init__(self,name,maxspeed,mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage

class bus(vehicle):
    def __init__(self, name, maxspeed, mileage,color):
        self.color = color
        vehicle.__init__(self,name,maxspeed,mileage)

v1 = bus("Tesla","I don't know",55,"White")
print("Taseen's fav car is",v1.name)
print("Taseen's fav color is",v1.color)

v2 = bus("BMW","I don't know",55,"Orange")
print("Vedanshi's fav car is",v2.name)
print("Vedanshi's fav color is",v2.color)













