sandwich_orders = ['pastrami', 'fish', 'pastrami', 'cabbage', 'pastrami', 'sala', 'pig', 'chicken']
finished_sandwich_orders = []
print(sandwich_orders)
print("'pastrami' soled out!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

while sandwich_orders:
    finished = sandwich_orders.pop()
    print("I made your " + finished + ' sandwich.')
    finished_sandwich_orders.append(finished)
print(sandwich_orders)
print(finished_sandwich_orders)