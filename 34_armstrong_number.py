# A number is an Armstrong Number or naracissitic number if it is equal to the sum of its own digits raised to power the number of digits

def armstrong_num (num) :

    # Creating a string form of the number
    num_str = str (num)
    num_lst = []
    
    # Iterating over the stringified integer
    for i in num_str :
        num_lst.append (int (i)) # Converting it back to integer before appending
    num_len = len (num_lst) # For the power

    total = 0

    for nums in num_lst :
        armstrong = nums ** num_len
        total += armstrong

    
    if (total == num) :
        result = f'\'{num}\' is an Armstrong number!'
        return result
    else :
        result = f'\'{num}\' is not an Armstrong number!'
        return result



print (armstrong_num (371))
print (armstrong_num (1634))
print (armstrong_num (20))




# Another Solution



def check_armstrong (num) :
    order = len (str (num))

    sum = 0

    # use twmp to find each digit. Then power it
    temp = num

    while (temp > 0) :
        digit = temp % 10
        sum += digit ** order
        temp //= 10


    return num == sum



num = int (input ('Enter your number: '))

if check_armstrong (num) :
    print (num, "is an Armstrong number")
else :
    print (num, "is not an Armstrong number")