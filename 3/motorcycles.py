#-*- coding:utf-8 -*-

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducadi'
print(motorcycles)
motorcycles.append('daguiwang')
print(motorcycles)
motorcycles.insert(0, 'xite')
print(motorcycles)
del motorcycles[0]
print(motorcycles)
motorcycles.pop()
print(motorcycles)
motorcycles.pop(0)
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'daguiwang', 'xite', 'xiaomianyang', 'xiaodi']
print(motorcycles)
moto_del = motorcycles.pop(1)
print(motorcycles)
print(moto_del)

motorcycles.remove('xite')
print(motorcycles)
_remove = 'suzuki'
motorcycles.remove(_remove)
print(motorcycles)
