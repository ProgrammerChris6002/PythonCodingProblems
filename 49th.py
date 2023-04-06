def nums_square(num):
    return num ** 2

nums = range(1,21)
squares = map(nums_square, nums)
print(list(squares))



# Another Solution


squaredNumbers = map(lambda x: x**2, range(1,21))
print(list(squaredNumbers))