class vehicles:
    def __init__(self, brand, year, milage, price):
        self.__brand = brand
        self.__year = year
        self.__milage = milage
        self.__price = price

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    @property
    def milage(self):
        return self.__milage

    @milage.setter
    def milage(self, value):
        self.__milage = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    def __str__(self) -> str:
        return f"Brand: {self.__brand}, Year: {self.__year}, Milage: {self.__milage}, Price: {self.__price}"


class Car(vehicles):
    def __init__(self, brand, year, milage, price, doors):
        super().__init__(brand, year, milage, price)
        self.__doors = doors

    @property
    def doors(self):
        return self.__doors

    @doors.setter
    def doors(self, value):
        self.__doors = value

    def __str__(self) -> str:
        return f"Brand: {self.brand}, Year: {self.year}, Milage: {self.milage}, Price: {self.price}, Doors: {self.__doors}"


class Truck(vehicles):
    def __init__(self, brand, year, milage, price, drive):
        super().__init__(brand, year, milage, price)
        self.__drive = drive

    @property
    def drive(self):
        return self.__drive

    @drive.setter
    def drive(self, value):
        self.__drive = value

    def __str__(self) -> str:
        return f"Brand: {self.brand}, Year: {self.year}, Milage: {self.milage}, Price: {self.price}, Drive: {self.__drive}"


class SUV(vehicles):
    def __init__(self, brand, year, milage, price, capacity):
        super().__init__(brand, year, milage, price)
        self.__capacity = capacity

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__capacity = value

    def __str__(self) -> str:
        return f"Brand: {self.brand}, Year: {self.year}, Milage: {self.milage}, Price: {self.price}, Capacity: {self.__capacity}"
