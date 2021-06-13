# -*- coding:utf-8 -*-

favorite_numbers = {
    'wangyue': 8,
    'liuseng': 2,
    'luoliuzhou': 9,
    'liushaoqiang': 1,
    'caohongsheng': 100,
    'xiongmao': 6,
    'xixi': 6,
}

peoples = ['liushaoqiang', 'xixi', 'wangermazi', 'liguoqiang']
for name in favorite_numbers.keys():
    if name in peoples:
        print("thanks " + name)
    else:
        print("xiacizailai " + name)

