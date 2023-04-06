def factorial (num):
    result = 1

    if (num == 0):
        return 1
    elif (num > 0):
        for i in range (1, num+1):
            result *= i
        return result
    else :
        return f'Invalid input!'
    

num = int (input ("Enter your number\n==> "))
print (factorial (num))




# Another Function



def fact (x):
    if (x == 0):
        return 1
    
    return x * fact (x - 1)


x = int (input ("Enter your number: "))
print (fact (x))