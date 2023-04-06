def cal_gcd (num1, num2) :
    gcd_lst = list ()

    num1_lst = []

    for i in range (1, num1+1) :
        if (num1 % i == 0) :
            num1_lst.append (i)


    num2_lst = []

    for i in range (1, num2+1) :
        if (num2 % i == 0) :
            num2_lst.append (i)

    for n in num1_lst :
        if (n in num2_lst) :
            gcd_lst.append (n)

    result = f'GCD of \'{num1}\' and \'{num2}\' is {max (gcd_lst)}'


    return result



print (cal_gcd (8, 12))




# Another Solution



def compute_gcd (x, y) :
    smaller = min (x, y)
    gcd = 1

    for i in range (1, smaller+1) :
        if ((x % i == 0) and (y % i == 0)) :
            gcd = i


    return gcd



num1 = int (input ('Enter first number: '))
num2 = int (input ('Enter second number: '))

gcd = compute_gcd (num1, num2)

print ("GCD of", num1, "and", num2, "is", gcd)




# Recursive GCD



def gcd (a, b) :
    if (b == 0) :
        return a
    else :
        return gcd (b, a%b)
    

a = int (input ('Enter first number: '))
b = int (input ('Enter second number: '))
GCD = gcd (a, b)

print ("GCD is: ", GCD)




# Built-in GCD



import math


a = int (input ('Enter first number: '))
b = int (input ('Enter second number: '))

gcd = math.gcd (a, b)
print (gcd)