def power (num1, num2) :
    square = num1 ** num2
    return square


num1 = int (input ('Enter a number: '))
num2 = int (input ('Enter a number: '))

print (power (num1, num2))




# Alternative Solution



def power_2 (base_num, power_num) :
    result = pow (base_num, power_num)
    return f'Your result is: {result}'


base_num = int (input ('Enter base: '))
power_num = int (input ('Enter power_num: '))

print (power_2 (base_num, power_num))