# -*- coding:utf-8 -*-

alien_0 = {"colo'r": 'green', "point": 5}
print(alien_0["colo'r"])
print(alien_0['point'])
new_points = alien_0['point']
print("You just earned " + str(new_points) + 'points.')
alien_0['x_point'] = 0
alien_0['y_point'] = 25
print(alien_0)
alien_1 = {}
alien_1['color'] = 'blue'
alien_1['point'] = 10
print(alien_1)

alien_2 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
if alien_2['speed'] == 'low':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_2['x_position'] = alien_2['x_position'] + x_increment
print(alien_2['x_position'])

del alien_2['speed']
print(alien_2)
