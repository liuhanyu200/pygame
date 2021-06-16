# coding:utf-8

def make_album(singer, album, amount=10):
    return {'singer': singer, 'album': album, 'amount': amount}


print(make_album('liudehua', '2021世界巡游', 100))
print(make_album('tianfuzhen', '心碎'))
print(make_album(singer='zhangjie', album='天下', amount=25))

all_singer = []

while True:
    singer = input("\nPlease input a singer you like: ")
    album = input("Please input a album of " + singer + ' ')
    amount = input("if you know amount of " + album + "input the number, if you don't know, input no. ")
    if amount != 'no':
        dic = make_album(singer, album, amount)
        all_singer.append(dic)
        print(dic)
    else:
        dic = make_album(singer, album)
        all_singer.append(dic)
        print(dic)
    flag = input("do you wan't to input another singer? (yes/no)")
    if flag == 'yes':
        continue
    else:
        break

print(all_singer)
