#-*- coding:utf-8 -*-
person = '\nAlice lili \t'
print('------------原名字----------------')
print(person, len(person))
print('------------去除左边的空格----------------')
print(person.lstrip(), len(person.lstrip()))
print('--------------去除右边的空格-------------')
print(person.rstrip(), len(person.rstrip()))
print('--------------去除全部空格-------------')
print(person.strip(), len(person.strip()))
print('-----------------------------')