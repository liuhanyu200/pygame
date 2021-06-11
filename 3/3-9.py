#-*- coding:utf-8 -*-

welcome_person = ['zhou bin', 'zhang ze fei', 'zou xue cai', 'lin xiao yong', 'luo liu zhou', 'liu shao xiang']
for person in welcome_person:
    print('welcome to my home to eat dinner,' + person)
print(welcome_person[4] + "don't have time!")
welcome_person[4] = 'qiu kui'
for person in welcome_person:
    print('welcome to my home to eat dinner,' + person)

print('I find a bigger zhuozi!')
welcome_person.insert(0, 'yan wei')
welcome_person.insert(3, 'xiong mao')
welcome_person.append('fa ge')
for person in welcome_person:
    print('welcome to my home to eat dinner,' + person)

print("I'm sorry to said that i can only welcome 2 people!")
while len(welcome_person) > 2:
    people = welcome_person.pop()
    print('sorry,' + people + '我们下次再约！')
for last_people in welcome_person:
    print('welcome to my home to eat dinner,' + last_people)

# print(range(len(welcome_person)))
print('-------------------')
print(len(welcome_person))
print('-------------------')
del welcome_person[0:2]

print(welcome_person)
print(type(welcome_person))