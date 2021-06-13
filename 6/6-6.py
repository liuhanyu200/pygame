# -*- coding:utf-8 -*-

favorite_numbers = {
    'wangyue': 8,
    'liuseng': 2,
    'luoliuzhou': 9,
    'liushaoqiang': 1,
    'caohongsheng': 100,
    'xiongmao': 6,
    'xixi': 6,
}
for name in favorite_numbers:
    print(name + "favorite number is " + str(favorite_numbers[name]) + '.')

# 遍历字典需要加上.items()
for name, number in favorite_numbers.items():
    print(name + "favorite number is " + str(number) + '.')

names = favorite_numbers.keys()
values = favorite_numbers.values()
print(names)
print(set(values))
print(type(names))
print(type(values))
