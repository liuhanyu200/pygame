# -*- coding:utf-8 -*-

users = {
    'aenstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for user, info in users.items():
    print("\nUsername: " + user)
    full_name = info['first'] + " " + info['last']
    location = info['location']
    print("fullname: " + full_name)
    print("location: " + location)