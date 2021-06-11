#-*- coding:utf-8 -*-

# 2.2 变量
message = "Hello Python world!"
print(message)
message = "现在的时间是：2021年6月11日21:07:18"
print(message)

# 2.3 字符串
name = "ada love lace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "love lace"
full_name = first_name + last_name
print(full_name)
print("Python:\nC:\nObject\n")
print(len('  python '))
print(len('  python '.rstrip()))
print(len('  python '.lstrip()))
print(len('  python '.strip()))

my_name = "my name's liuhanyu"
the_name = 'my "name" is liuhanyu'

# 2.4 数字
print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 3)
print(2 % 3)
# 乘方
print(2 ** 3)
# 次序
print(2 + 3 ** 2 / 2 -1)
print(0.1 + 0.2) # 小数位数不确定，不用担心

age = 23
print("Happy " + str(age) + 'rd Birthday!')
print(3 / 2)
print(3 / 2.0)

