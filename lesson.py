class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year


    def display_info(self):
        print(f"Brand:{self.brand}, Year:{self.year}")


class Car(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand, year)



class Motorcycle(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand, year)



car = Car('Toyota', '2024')
motorcycle = Motorcycle('Bugatti', '2022')


car.display_info()
print()
motorcycle.display_info()





