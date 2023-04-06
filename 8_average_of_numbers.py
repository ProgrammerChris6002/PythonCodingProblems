def average_of_nums (*nums) :
    total = 0
    nums_lst = []

    for num in nums :
        total += num
        nums_lst.append (num)

    result = f'{total / len (nums_lst):.3}'


    return result



num1 = int (input ('Enter first number: '))
num2 = int (input ('Enter second number: '))
num3 = int (input ('Enter third number: '))

print (average_of_nums (num1, num2, num3))




# Method Two



def average_of_nums_2 (nums) :
    nums_lst = list ()

    for i in range (nums) :
        num = int (input ('Enter a number: '))
        nums_lst.append (num)

    sum_of_nums = sum (nums_lst)
    result = f'Average: {sum_of_nums / nums:.4}'


    return result



nums = int (input ('How many numbers do you want to enter: '))

print (average_of_nums_2 (nums))




# Another Solution



def average_of_nums_3 (nums) :
    total = 0

    for i in range (nums) :
        elem = int (input ('Enter element: '))
        total += elem

    avg = total / nums


    return avg



nums = int (input ('How many numbers do you want to enter: '))

print (average_of_nums_3 (nums))