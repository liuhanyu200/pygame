### 前言

如果你编程技艺无穷，你打算开发什么样的程序呢？
你就要开始学习编程了
如果心中有目标，就能立即将新学到的技能付诸应用
现在正是草拟目标的大好时机
将想法记录下来是个不错的习惯
这样每当需要开始新项目时，都可参考它们
现在请花点时间描绘三个你想创建的程序

我学习的幻想：

1、做一个类似星露谷物语的游戏

2、爬、窃取关注的人、物、事的数据，分析学习，产出一个个具有不同属性的个体

3、万物互联

### 第二章 变量和简单数据类型
变量只能以字母或下划线打头，只能包含数字、字母和下划线
慎用小写字母l和大写字母O，容易被看错成1和0
变量名应该简短又具有描述性
就目前而言，python中应使用小写字母，不建议使用大写字母
Python使用加号（ +）来合并字符串
方法lower()很有用。很多时候，你无法依靠用户来提供正确的大小写，因此需要将字符串先转换成小写，再存储它们。以后需要显示这些信息时，再将其转换为最合适的大小写方式

### 第三章 列表简介
在python中用方括号（[]）来表示列表，并用逗号来隔开其中的元素。
`bicycles = ['trek', 'redline', 'specialized']`

在python中，列表元素的索引为0，而不是1

`print(bicycle[0]) # trek`

append()、pop()、insert()、del、remove()、reverse、sort、sorted() 
### 第六章 字典
遍历字典中的值
`for key, value in favorite_numbers.items():
    print(name + "favorite number is " + str(number) + '.')`

### 内置函数

![image-20210615113211280](C:\Users\klci\AppData\Roaming\Typora\typora-user-images\image-20210615113211280.png)

内置函数调用直接写函数名传递参数即可，方法的调用则需要先将类实例化，通过.调用方法

#### 循环

break

continue  参考 7/counting.py 和 7-5.py

### 函数

使用函数默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参

基于元组的可变参数

`def make_pizza(size, *toppings):`

传参方式：

1、直接传

`make_pizza(22, "cheese", "milk", "butter", "fish")`

2、传元组

`make_pizza(22, ("cheese", "milk", "butter", "fish"))`

基于字典可变参数

传参顺序：

**必选参数、默认参数、可变参数和关键字参数**

