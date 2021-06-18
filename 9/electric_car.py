# coding:utf-8
from car import *
from battery import *


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
        self.battery = Battery()

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "kWh battery.")

    # 由于增加了参数，从而改变了同父类方法的一致性违反了LSP原则（在使用父类的场景，替换为子类也一样可行）。
    # 解决方式为，在子类重写的方法中为参数里添加默认值赋值，这样就确保了父类方法中定义的参数在子类中一定不会失效
    # 从而确保了自上而下的一致性。self=None
    @staticmethod
    def fill_gas_tank(self=None) -> None:
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
