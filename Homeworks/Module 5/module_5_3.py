class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        if isinstance(other, Building):
            return (self.numberOfFloors == other.numberOfFloors and
                    self.buildingType == other.buildingType)
        return False


building1 = Building(2, 'Small house')
building2 = Building(2, 'Small house')
building3 = Building(10, 'Big house')

print(building1 == building2)
print(building1 == building3)
