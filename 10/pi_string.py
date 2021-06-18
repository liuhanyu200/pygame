# coding:utf-8

with open('./data/pi_million_digits.txt') as file_object:
    data = file_object.read()
    print(data[:52])
    birthday = '930731'
    if birthday in data:
        print("yes")
    else:
        print("no")
