# coding:utf-8

def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians, new_magicians=[]):
    while magicians:
        magician = "The great " + magicians.pop()
        # print(magician)
        new_magicians.append(magician)
    return new_magicians


magicians = ['liuqian', 'wanghan', 'dulei']
new_magicians = []
make_great(magicians[:], new_magicians)
print(magicians)
print(new_magicians)
