# coding:utf-8

class Restaurant(object):
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

    def describe_restaurant(self):
        print("restaurant name is " + self.restaurant_name)
        print("cuisine_type is " + self.cuisine_type)

    @staticmethod
    def open_restaurant() -> None:
        print("restaurant is now business ing!")


restaurant = Restaurant('丽水云泉大酒店', 'duck')
restaurant.set_number_served(100)
print(restaurant.number_served)
restaurant.increment_number_served(22)
print(restaurant.number_served)
