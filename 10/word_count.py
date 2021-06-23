# coding:utf-8

def word_count(filename):
    word_length = 0
    try:
        with open(filename) as f_obj:
            content = f_obj.read()
    except FileNotFoundError:
        print("File Not Found.")
    else:
        word = content.split()
        word_length = len(word)
    return word_length


a = word_count('./data/alice.txt')
print(a)
