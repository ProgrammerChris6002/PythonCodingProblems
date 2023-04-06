def check_even (num):
    if (num % 2 == 0):
        return f'{num} is an even number.'
    return f'{num} is an odd number.'

num = int (input ("Enter your number\n==> "))
print (check_even (num))



# Another Solution


def checkValue (n):
    if (n%2 == 0):
        print ("It is an even number")
    else:
        print ("It is an odd number")

checkValue (7)