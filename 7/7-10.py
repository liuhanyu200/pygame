# coding:utf-8
name_promote = "What's your name? "
place_promote = "If you could visit a place, where would you go?"
flag = True
favorite_flace = {}
while flag:
    name = input(name_promote)
    place = input(place_promote)
    favorite_flace[name] = place
    _exit = input("anyone wan't to next ? no to exit .")
    if _exit == 'no':
        flag = False
    else:
        continue
print(favorite_flace)
