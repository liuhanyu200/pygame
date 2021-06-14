# -*- coding:utf-8 -*-

favorite_languages = {
    'liuhanyu': 'python',
    'linxiaoyong': 'java',
    'huangwenjun': 'java',
    'zhouzihao': 'php',
    'lengyang': 'C',
}

print("huangwenjun's favorite language is " + favorite_languages['huangwenjun'].title() + '.')

favorite_languages2 = {
    'jen': ['python', 'ruby'],
    'sara': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages2.items():
    print(name + "favorite language are:")
    for language in languages:
        print('\t' + language.title())