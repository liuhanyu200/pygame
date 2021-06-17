# coding:utf-8

def make_sandwich(*toppings):
    for topping in toppings:
        print("You orderd a " + topping)


# 1、直接调用
make_sandwich('fish', 'cabbage', 'salad')
# 2、通过turple调用
tps = ('fish', 'cabbage', 'salad', 'fanqiejiang')
make_sandwich(*tps)
