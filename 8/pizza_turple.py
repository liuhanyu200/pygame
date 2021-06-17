# coding:utf-8

def make_pizza(size, *toppings):
    for topping in toppings:
        print(topping)


make_pizza(16, "cheese")
make_pizza(22, "cheese", "milk", "butter", "fish")
make_pizza(12, ('a', 'b', 'c'))
tps = ('a', 'b', 'c')
make_pizza(12, *tps)
