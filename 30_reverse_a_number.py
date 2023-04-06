def rev_num (num) :
    nums = []

    while (num >= 1) :
        nums.append (num % 10)
        num = num // 10

    result = ''

    for i in nums :
        result += str (i)


    return f'Reverse: {result}'



num = int (input ('Enter number to be reversed: '))

print (rev_num (num))




# Another Solution



def reverse_num (num) :
    reverse = 0

    while (num > 0) :
        last_digit = num % 10
        reverse = (reverse * 10) + last_digit
        num = num // 10


    return reverse



n = int (input ('Enter number: '))
reverse = (reverse_num (n))

print ("Reverse of the number:", reverse)