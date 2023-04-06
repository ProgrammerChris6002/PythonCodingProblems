def max_of_two_nums (num1, num2) :
    if (num1 > num2) :
        return ('Max: {}'.format (num1))
    
    return ('Max: %d'% (num2))


num1 = int (input ('Enter first number: '))
num2 = int (input ('Enter second number: '))

print (max_of_two_nums (num1, num2))




# Shortcut



def max_of_two_nums_2 (num1, num2) :
    result = max (num1, num2)
    
    return f'Max: {result}'


num1 = int (input ('Enter first number: '))
num2 = int (input ('Enter second number: '))

print (max_of_two_nums_2 (num1, num2))