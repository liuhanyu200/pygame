# coding:utf-8

class User(object):
    def __init__(self, first_name, last_name, **describes):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
        self.describes = {}
        for key, value in describes.items():
            self.describes[key] = value

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print(self.describes)

    def greet_user(self):
        print("Hello " + self.first_name + ' ' + self.last_name)


des = {'habit': 'game', 'location': 'Kunming', 'country': 'China'}
user = User('liu', 'hand', **des)
for fail_number in range(10):
    user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)
