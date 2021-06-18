# coding:utf-8

class Privileges(object):
    def __init__(self, privileges):
        self.privileges = privileges
        self.privileges = ['add', 'delete', 'modify', 'inquire']

    def show_privileges(self):
        for privilege in self.privileges:
            print("You have " + privilege + 'Authority' + '.')

