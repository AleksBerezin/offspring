print ("Hi, it's me again. Thank you for helping with the first task. Today you need to check the second task. Let's get started.")
print ()
print ('''You can use next operation: 
Press + for addition
Press - for subtraction
Press * for multiplication
Press / for division''')

num1 = float(input('Enter value: '))
operation = input('Enter operation: ')
num2 = float(input('Enter new value: '))
if operation == '/' and num2 == '0':
    print('Division by zero, bad idea. Try again')
print('{} {} {} = '.format(num1 , operation , num2))

if operation == '/':
    res = float(num1) / float(num2)
if operation == '+':
    res = float(num1) + float(num2)
if operation == '-':
    res = float(num1) - float(num2)
if operation == '*':
    res = float(num1) * float(num2)
print(f'Intermediate result: {res}')

while operation != '':
    operation = input('Enter operation: ')
    num2 = input('Enter new value: ')
    if operation == '+':
        res = res + float(num2)
    if operation == '-':
        res = res - float(num2)
    if operation == '/':
        res = res / int(num2)
    if operation == '*':
        res = res * float(num2)
    print(f"Intermediate result: {res}")
print(f"Result: {res}")
