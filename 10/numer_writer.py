# coding:utf-8

import json

numbers = [1, 2, 3, 4, 5, 6, 7]
filename = './data/numbers.json'
with open(filename, 'a') as f_obj:
    json.dump(numbers, f_obj)
