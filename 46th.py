def square_nums(num):
    return num * num

nums = [1,2,3,4,5,6,7,8,9,10]
squares = map(square_nums, nums)
print(list(squares))



# Another Solution


li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x: x**2, li)
print(list(squaredNumbers))