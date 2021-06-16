# coding:utf-8

def describe_pet(animal_type='dog', pet_name='xialuo'):
    print("\nI have a " + animal_type + '.')
    print("His name is " + pet_name.title() + '.')


# 位置传参
describe_pet('dog', 'daxiong')
describe_pet('pig', 'xialuo')
# 使用默认参数
describe_pet()

# 关键字传参
describe_pet(pet_name='xiaoluo', animal_type='spider')
