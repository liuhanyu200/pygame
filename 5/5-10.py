# -*- coding:utf-8 -*-

current_users = ['Admin', 'ZhouZiHao', 'Liuhanyu', 'Yinhaoquan', 'zhoubin', 'huangwenjun']
new_users = ['admin', 'liuHanyu', 'shanze', 'Zhangsan', 'Luoliuzhou', 'zhanglei']

current_users_lower = []

for current_user in current_users:
    current_users_lower.append(current_user.lower())

for user in new_users:
    if user.lower() in current_users_lower:
        print(user + "已经被使用了,请换一个！")
    else:
        print("恭喜你,用户名：" + user + " 可用！")

print(current_users_lower)