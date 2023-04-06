def divisible_3_5 (num) :
    nums_lst = list ()

    for nums in range (15, num+1) :
        if (nums%3 == 0) and (nums%5 == 0) and (num>=15) :
            nums_lst.append (nums)


    return nums_lst



num = int (input ('Enter a number: '))

print (divisible_3_5 (num))