def floor_div (num1, num2) :
    result = num1 // num2

    return result



num1 = int (input ('Enter first number: '))
num2 = int (input ('Enter second number: '))

print (floor_div (num1, num2))




# Think Different



import math

result = math.floor (3.4)
print (result)




# Alternative Solution



def floor_div_2 (num1, num2) :
    result = math.floor (num1 / num2)

    return result


num1 = int (input ('Enter first number: '))
num2 = int (input ('Enter second number: '))

print (floor_div_2 (num1, num2)) 