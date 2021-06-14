# -*- coding:utf-8 -*-

citys = {
    'kunming': {
        'country': 'China',
        'population': 14000000,
        'fact': 'elephint in kunming',
    },
    'beijing': {
        'country': 'China',
        'population': 2400000,
        'fact': 'changcheng in beijing',
    },
    'shanghai': {
        'country': 'China',
        'population': 5000000,
        'fact': 'shanghai is the famous city',
    },
}
for city, info in citys.items():
    print("City: " + city)
    print(city + " is in " + info['country'] + '.')
    print('population: ' + str(info['population']))
    print('the fact of ' + city + ' is : ' + info['fact'])