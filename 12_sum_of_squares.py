def sum_squares (num) :
    result = 0

    for i in range (num+1) :
        result += i ** 2


    return result



print (sum_squares (5))




# Shortcut



def sum_squares_2 (num) :
    result = int (((num) * (num+1) * (2*num+1) / (6)))

    return result


print (sum_squares_2 (5))