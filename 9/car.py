# coding:utf-8

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self) -> str:
        long_name = self.year + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        print("Your car has " + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_new_car = Car('东风本田', 'civic', '2017')
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# my_new_car.odometer_reading = 20001
# my_new_car.read_odometer()
# my_new_car.update_odometer(22)
# my_new_car.read_odometer()
my_new_car.increment_odometer(55)
my_new_car.read_odometer()
