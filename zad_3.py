class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"{self.__class__.__name__} Lokalizacja: {self.address} Area: {self.area} m^2 Pokoje: {self.rooms} rooms. Cena: {self.price} PLN"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor


house1 = House(150, 4, 500000, "Warszawa Wiejska 1", 300)
flat1 = Flat(75, 2, 200000, "Katowice Sądowa 1", 4)

print(house1)
print(flat1)
