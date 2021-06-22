# coding:utf-8

filname = 'alice.txt'

try:
    with open(filname) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("File Not Found.")
