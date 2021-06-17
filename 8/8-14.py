# coding:utf-8

def cars(manufacturer, model, **descriptions):
    car = {'manufacturer': manufacturer, 'model': model}
    for key, value in descriptions.items():
        car[key] = value
    return car


des = {'displacement': '1.5T', 'sell price': 138000, 'weight': '1.2吨'}
new_car = cars('东风本田', 'civic2020', **des)
print(new_car)
