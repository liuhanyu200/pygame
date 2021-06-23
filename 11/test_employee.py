import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee('liu', 'hanyu', employee=100000)

    def test_give_default_raise(self):
        self.default_employee = self.my_employee.give_raise()
        self.assertEqual(self.my_employee.employee, self.default_employee)

    def test_give_custom_raise(self):
        self.custom_employee = self.my_employee.give_raise(money=10000)
        self.assertEqual(self.my_employee.employee, self.custom_employee)


if __name__ == '__main__':
    unittest
