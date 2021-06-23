# coding:utf-8

filname = './data/alice.txt'

try:
    with open(filname) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("File Not Found.")
else:
    words = contents.split()
    num_words = len(words)
print("长度：" + str(num_words))
