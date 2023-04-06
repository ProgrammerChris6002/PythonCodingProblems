def prime_number (num):
    for i in range(2, num) :
        if num % i == 0:
            return False
    return True


def prime_numbers (num) :
    num = int(input('Enter number limit: '))
    all_prime_nums = []
    for i in range (2, num+1) :
        if prime_number(i) == True:
            all_prime_nums.append(i)
    primes = f'Prime numbers between 0 and {num} are: \n {all_prime_nums}'
    return primes

print(prime_numbers(10))