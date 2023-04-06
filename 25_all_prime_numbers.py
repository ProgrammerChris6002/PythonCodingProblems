def is_prime (num) :
    for i in range (2, num) :
        if (num % i == 0) :
            return False

    return True




def all_primes (num) :
    primes = list ()

    for i in range (2, num+1) :
        if (is_prime (i) is True) :
            primes.append (i)


    return primes



print (all_primes (7))