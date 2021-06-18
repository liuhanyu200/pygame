# coding:utf-8

with open('./data/pi_digits.txt') as file_object:
    # content = file_object.read()
    # print(content)
    lines = file_object.readlines()
    all_line = ''
    for line in lines:
        all_line += line.strip()
    print(all_line)
