# coding:utf-8

with open('./data/guest.txt', 'a') as fileobjct:
    guest = input("Please input your name: ")
    fileobjct.write(guest + '\n')
