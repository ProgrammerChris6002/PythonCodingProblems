def simple_cal ():
    operations = ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Exponentiation', 'Modulus', 'Floor Division']
    operators = ['+', '-', '*', '/', '\uB002', '%', '//']
    print ('What operation will you like to perform?\n')

    for i, item in enumerate (operations):
        print (i+1, item)
    opera = int (input (f'==> '))

    a = int (input ("Enter first number==> "))
    b = int (input ("Enter second number==> "))


    if (opera == 1):
        return f'{a} {operators[0]} {b} = {a+b}'
    elif (opera == 2):
        return f'{a} {operators[1]} {b} = {a-b}'
    elif (opera == 3):
        return f'{a} {operators[2]} {b} = {a*b}'
    elif (opera == 4):
        return f'{a} {operators[3]} {b} = {a/b}'
    elif (opera == 5):
        return f'{a} {operators[4]} {b} = {a**b}'
    elif (opera == 6):
        return f'{a} {operators[5]} {b} = {a%b}'
    elif (opera == 7):
        return f'{a} {operators[6]} {b} = {a//b}'
    


print (simple_cal ())





# Aother Solution




def add (num1, num2):
    return num1 + num2

def subtract (num1, num2):
    return num1 - num2

def multiply (num1, num2):
    return num1 * num2

def divide (num1, num2):
    return num1 / num2

def modulo (num1, num2):
    return num1 % num2



# Take input from the user

num1 = int (input ("Enter first number: "))
operation = input ("What you want to do(+, -, *, /, %): ")
num2 = int (input ("Enter second number: "))


result = 0

if (operation == '+'):
    result = add (num1, num2)
elif (operation == '-'):
    result = subtract (num1, num2)
elif (operation == '*'):
    result = multiply (num1, num2)
elif (operation == '/'):
    result = divide (num1, num2)
elif (operation == '%'):
    result = modulo (num1, num2)
else:
    print ("Please enter: +, -, *, / or %")


print (num1, operation, num2, '=', result)