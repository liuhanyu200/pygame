# coding:utf-8

class Privileges(object):
    def __init__(self):
        self.privilege = ['add', 'delete', 'modify', 'inquire']

    def show_privileges(self):
        for pl in self.privilege:
            print("123You have " + pl + 'Authority' + '.')

