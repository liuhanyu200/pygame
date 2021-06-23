# coding:utf-8

def cat_dog(filename1, filename2):
    try:
        with open(filename1) as f_obj1:
            f_obj1_content = f_obj1.read()
        with open(filename2) as f_obj2:
            f_obj2_content = f_obj2.read()
    except FileNotFoundError:
        # print("File Not Found.")
        pass
    else:
        print(f_obj1_content + '\n' + f_obj2_content)


cat_dog('../data/cats.txt', './data/dogs.txt')
