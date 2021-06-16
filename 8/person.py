# coding:utf-8

def build_person(first_name, last_name):
    return {'first_name': first_name, 'last_name': last_name}


print(build_person('Saber', 'Lily'))

while True:
    print("\nPlease tell me your name:")
    f_name = input('first_name')
    l_name = input('last_name')
    _exit = input("Print q to exit!")
    if _exit == 'q':
        break

print(build_person(f_name, l_name))
