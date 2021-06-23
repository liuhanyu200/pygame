# coding:utf-8
import unittest
from city_country import get_city_country


class CityCountryTest(unittest.TestCase):
    def test_city_country(self):
        formatted = get_city_country('kunming', 'china')
        self.assertEqual(formatted, 'Kunming, China')

    def test_city_country_population(self):
        formatted = get_city_country('puer', 'China', 2000000)
        self.assertEqual(formatted, 'Puer, China 2000000')


if __name__ == '__main__':
    unittest
