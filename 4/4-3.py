#-*- coding:utf-8 -*-

for number in range(1,21):
    print(number)

nums = [x for x in range(1, 1000001)]
# for num in nums:
#     print(num)
print(min(nums))
print(max(nums))
print(sum(nums))

_lists = [x for x in range(1, 20, 2)]
print(_lists)
for _list in _lists:
    print(_list)
