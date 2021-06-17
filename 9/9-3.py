# coding:utf-8

class User(object):
    def __init__(self, first_name, last_name, **describes):
        self.first_name = first_name
        self.last_name = last_name
        self.describes = {}
        for key, value in describes.items():
            self.describes[key] = value

    def describe_user(self):
        print(self.describes)

    def greet_user(self):
        print("Hello " + self.first_name + ' ' + self.last_name)


des = {'habit': 'game', 'location': 'Kunming', 'country': 'China'}
user = User('liu', 'hand', **des)
user.describe_user()
user.greet_user()
