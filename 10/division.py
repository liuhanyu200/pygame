# coding:utf-8

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("Give me two numbers, I'll divide them.")
print("Print q to exit.")
number1 = input("First number: ")
number2 = input("Second number: ")


