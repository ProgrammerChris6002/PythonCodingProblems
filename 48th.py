def get_nums(num):
    if (num % 2 == 0):
        return True
    return False
    
nums = range(1,21)
even_nums = filter(get_nums, nums)
print(list(even_nums))



# Another Solution


evenNumbers = filter(lambda x: x%2==0, range(1,21))
print(list(evenNumbers))