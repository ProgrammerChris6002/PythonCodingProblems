def sum_two_nums_str (num1, num2):
    return f'{num1} + {num2} = {int(num1) + int(num2)}'

num1 = input ("Enter your first number\n==> ")
num2 = input ("Enter your first number\n==> ")
print (sum_two_nums_str (num1, num2))



# Another Solution


def printValue (s1,s2):
    print (int (s1) + int (s2))

printValue ("3", "4")