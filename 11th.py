def bin_num (nums):
    lst = []

    for num in nums.split (','):
        if (int (num) % 5 == 0) and (int (num[0]) != 0):
            lst.append (num)

    if (len (lst) == 0):
        return 'None of them is/are divisible by 5'
    elif (len (lst) == 1):
        result = ''.join (lst)
        return result
    elif (len (lst) > 1): 
        result = ','.join (lst)
        return result
    


nums = input ("Enter numbers as comma seperated values\n==> ")
print (bin_num (nums))





# Another Solution



value = []
items=[x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print(','.join(value))


# Binary to Decimal
x=[1,11, 101, 111]

for i in x:
    print (int (str (i), 2))