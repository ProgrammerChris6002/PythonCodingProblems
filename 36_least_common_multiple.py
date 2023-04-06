def cal_lcm (num1, num2) :
    multiple = num1 * num2
    multiple_lst = []
    cm_lst = list ()

    for i in range (1, multiple+1) :
        if (multiple % i == 0) :
            multiple_lst.append (i)

    for nums in multiple_lst :
        if (nums % num1 == 0) and (nums % num2 == 0) :
            cm_lst.append (nums)

    lcm = min (cm_lst)


    return lcm


print (cal_lcm (10, 8))




# Another Solution



def calculate_lcm (x, y) :
    lcm = max (x, y)

    while (lcm % x != 0) or (lcm % y != 0) :
        lcm += 1


    return lcm



num1 = int (input ('First number: '))
num2 = int (input ('Second number: '))
lcm = calculate_lcm (num1, num2)

print (f'LCM of {num1} and {num2} is: {lcm}')