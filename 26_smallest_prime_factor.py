def is_prime (num) :
    for i in range (2, num) :
        if (num % i == 0) :
            return False

    return True




def smallest_prime_fac (num) :
    factors = []

    for i in range (2, num) :
        if (num % i == 0) and (is_prime (i) is True) :
            factors.append (i)

    smallest = min (factors)
    print (factors)


    return f'Smallest prime factor: {smallest}'



print (smallest_prime_fac (10))




# Another Solution



def get_smallest_factor (num) :
    factor = 2

    while (num % factor != 0) :
        factor += 1


    return factor



num = int (input ('Enter your number: '))

smallest_factor = get_smallest_factor (num)
print ('The smallest factor is:', smallest_factor)