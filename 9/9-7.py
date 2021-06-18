# coding:utf-8
from user import User


class Admin(User):
    def __init__(self, first_name, last_name, **describes):
        super().__init__(first_name, last_name, **describes)
        self.privileges = ['add', 'delete', 'modify', 'inquire']

    def show_privileges(self):
        for privilege in self.privileges:
            print("You have " + privilege + ' Authority' + '.')


des = {'habit': 'game', 'location': 'Kunming', 'country': 'China'}
new_user = Admin('liu', 'hanyu', **des)
new_user.show_privileges()
