# -*- coding:utf-8 -*-

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

_aliens = []
for i in range(30):
    a = {'color': 'green', 'points': 5, 'speed': 'low'}
    _aliens.append(a)

for _alien in _aliens[:5]:
    print(alien)
print('...')

for _alien in _aliens[:3]:
    if _alien['color'] == 'green':
        _alien['color'] == 'yellow'
        _alien['speed'] == 'medium'
        _alien['points'] == 10

for _alien in _aliens[:5]:
    print(alien)
print('...')







