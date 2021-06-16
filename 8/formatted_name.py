# coding:utf-8

def get_formatted_name(first_name, last_name, middle_name=''):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()


name = get_formatted_name('Saber', 'Lily')
print(name)
print(get_formatted_name('luo', 'liu', 'zhou'))
