# coding:utf-8

unconfirmed_users = ['liuhanyu', 'luoliuzhou', 'wangyue', 'xiaolizi']
confirmed_users = []

while unconfirmed_users:
    user = unconfirmed_users.pop()
    confirmed_users.append(user)
print(confirmed_users)
print(unconfirmed_users)