class Car:
    def __init__(self, name, year, hp):
        self.name= "Audi A1 Sportback"
        self.year = year
        self.hp = hp

    def print_car(self):
        print("The name of my car is: ", self.name)

    def print_hp(self):
        print("The name of my car is: ", self.hp, "hp's.")

my_car = Car("Audi A1 Sportback 40 TFSI", "2020", "200")
my_car.print_car()
my_car.print_hp()

my_car2 = Car("Opel Insignia", "2020", "120")
my_car2.print_car()
my_car2.print_hp()
