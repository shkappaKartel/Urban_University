class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print('Количество этажей: ', self.numberOfFloors)


house = House()
house.setNewNumberOfFloors(10)