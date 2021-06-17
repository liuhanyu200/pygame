# coding:utf-8

def user_profiles(first, last, **toppings):
    profile = {'first': first, 'last': last}
    for key, value in toppings.items():
        profile[key] = value
    return profile


user_profile = user_profiles('li', 'fei', location='kunming', city='beijing')
# print(user_profile)
user_profile = user_profiles('li', 'fei', toppings={'location': 'kunming', 'city': 'beijing'})

tps = {'location': 'kunming', 'city': 'beijing'}
user_profile = user_profiles('li', 'fei', **tps)
print(user_profile)
