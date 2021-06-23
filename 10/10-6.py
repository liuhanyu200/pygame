# coding:utf-8

def add_two_numbers():
    while True:
        try:
            first_number = input("请输入两个数，我帮你做加法运算。（回车结束）第一个：")
            second_number = input("第二个：")
            first_number = int(first_number)
            second_number = int(second_number)
        except ValueError:
            print("请输入数字！")
            continue
        else:
            result = first_number + second_number
            print(result)
            break


add_two_numbers()
