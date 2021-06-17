# coding:utf-8

def greet_users(names):
    for name in names:
        greet = "Hello, " + name.title() + '!'
        print(greet)


user_list = ['lifei', 'zhanglei', 'dulei', 'shanze']
greet_users(user_list)
