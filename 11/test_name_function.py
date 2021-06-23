# coding:utf-8

import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin', 'dulei')
        self.assertEqual(formatted_name, 'Janisjoplindulei')


unittest.main
