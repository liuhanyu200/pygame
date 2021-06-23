# coding:utf-8

def count_word(filename, keywords):
    try:
        with open(filename) as f_obj:
            content = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        words = content.split()
        length = len(words)
        key = content.lower().count(keywords)
        # key = content.count(keywords)
    return key


result = count_word('./data/The Incomplete Theft.txt', 'the')
print(result)
