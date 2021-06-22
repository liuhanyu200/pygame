# coding:utf-8

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("Give me two numbers, I'll divide them.")
print("Print q to exit.")
while True:
    number1 = input("First number: ")
    if number1 == 'q':
        break
    number2 = input("Second number: ")
    if number2 == 'q':
        break
    try:
        answer = int(number1) / int(number2)
    except ZeroDivisionError:
        pass
    else:
        print(answer)
