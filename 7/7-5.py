# coding:utf-8
promote = "\nHow old are you?"
promote += "\n Enter quit to quit."

active = True
while active:
    age = input(promote)
    if age == 'quit':
        active = False
        continue
    if age != 'quit':
        age = int(age)
    if age < 3:
        print("free")
    if 3 < age < 12:
        print("$10")
    if age >= 12:
        print("$15")
