def square (num):
    result = f' The square of {num} = {num ** 2}'
    return result

num = int (input ("Enter number to be squared\n==> "))
print (square (num))



# Another Solution


def square_2 (num):
    return num ** 2

print (square_2 (2))
print (square_2 (3))


print (help ())