# coding:utf-8
while True:
    name = input("Please input your name: ")
    with open('./data/guest_book.txt', 'a') as gb:
        gb.write('Hello, ' + name.title() + ", why do you like programming? " + '\n')
        reason = input("Why do you like programming? ")
        gb.write(reason + '\n')
    _exit = input("input exit to quit.")
    if _exit == 'exit':
        break
    else:
        continue
