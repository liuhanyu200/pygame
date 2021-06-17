# coding:utf-8

class Restaurant(object):
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("restaurant name is " + self.restaurant_name)
        print("cuisine_type is " + self.cuisine_type)

    @staticmethod
    def open_restaurant() -> None:
        print("restaurant is now business ing!")


restaurant = Restaurant('丽水云泉大酒店', 'duck')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
