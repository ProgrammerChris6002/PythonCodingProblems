def odd_num (nums):
    lst = [i for i in nums.split (',') if (int (i) % 2 != 0)]
    result = ','.join (lst)

    return f'Odds = {result}'


num = input ("Enter your integer(s) as comma seperated values\n==> ")
print (odd_num (num))




# Another Solution



values = input ("Enter your integer(s) as comma seperated values\n==> ")

numbers = [x for x in values.split (',') if int(x)%2 != 0]

print (",".join (numbers))