# -*- coding:utf-8 -*-

message = "\ntell me something, I'll tell you the same thing.\n"
message += "\n Enter quit to exit program!"

messages = ""
active = True

while messages != 'quit':
    messages = input(message)
    if messages == 'quit':
        active = False
    else:
        print(messages + '\n')