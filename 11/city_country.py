# coding:utf-8

def get_city_country(city, country, population=''):
    if population:
        result = city.title() + ', ' + country.title() + ' ' + str(population)
    else:
        result = city.title() + ', ' + country.title()
    return result
