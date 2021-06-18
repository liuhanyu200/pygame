# coding:utf-8

class Battery(object):
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
        self.range = 0

    def describe_battery(self):
        print("222This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            self.range = 240
        elif self.battery_size == 85:
            self.range = 270
        message = "This car can go approximately " + str(self.range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

