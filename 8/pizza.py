# coding:utf-8

def make_pizza(*toppings):
    for topping in toppings:
        print(topping)


make_pizza("cheese")
make_pizza("cheese", "milk", "butter", "fish")
