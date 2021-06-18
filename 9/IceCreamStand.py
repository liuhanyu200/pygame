# coding:utf-8
from restaurant import Restaurant as Rs


class IceCreamStand(Rs):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['strawberry', 'vanilla', 'milk', 'durian']

    def describe_flavors(self):
        for flavor in self.flavors:
            print("We have " + flavor + "IceCream")


new_ice = IceCreamStand('大维', 'fish')
new_ice.describe_flavors()
