class Employee(object):
    def __init__(self, first_name, last_name, employee):
        self.first_name = first_name
        self.last_name = last_name
        self.employee = employee

    def give_raise(self, money=5000):
        self.employee += money
        return self.employee
