# coding:utf-8

responses = {}
flag = True
while flag:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    next = input('continue ?')
    if next == 'no':
        flag = False
print("\n--- Poll Results ---")
print(responses)