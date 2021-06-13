# -*- coding:utf-8 -*-

pizzas = ['fruit', 'buff', 'milk', 'zhishi', 'little']
# for pizza in pizzas:
#     print(pizza)
#     print(pizza.title() + ", I like eat !")
# print("I like eat pizza!")
pizzas_bak = pizzas[:]
pizzas.append('chicken')
pizzas_bak.append('dog')
print(pizzas_bak)
print(pizzas)