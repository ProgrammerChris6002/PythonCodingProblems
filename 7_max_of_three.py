def max_of_three_nums (num1, num2, num3) :
    result = max (num1, num2, num3)

    return f'Max: {result}'


num1 = int (input ('Enter first number: '))
num2 = int (input ('Enter second number: '))
num3 = int (input ('Enter third number: '))

print (max_of_three_nums (num1, num2, num3))




def max_of_three_nums_2 (num1, num2, num3) :
    if (num1 >= num2) and (num1 >= num3) :
        return f'Max: {num1}'

    elif (num2 >= num1) and (num2 >= num3) :
        return f'Max: {num2}'

    return 'Max: {}'.format (num3)


num1 = int (input ('Enter first number: '))
num2 = int (input ('Enter second number: '))
num3 = int (input ('Enter third number: '))

print (max_of_three_nums_2 (num1, num2, num3))