# coding:utf-8
from user import User
from privilege import Privileges


class Admin(User):
    def __init__(self, first_name, last_name, **describes):
        super().__init__(first_name, last_name, **describes)
        self.privileges = ['add', 'delete', 'modify', 'inquire']
        self.privilege = Privileges()

    def show_privileges(self):
        for privilege in self.privileges:
            print("You have " + privilege + 'Authority' + '.')


new_user = Admin('liu', 'hanyu')
new_user.privilege.show_privileges()