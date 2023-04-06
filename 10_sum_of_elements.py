def sum_elements (lst) :
    result = sum (lst)

    return result


print (sum_elements ([1, 2, 3, 4, 5]))



# Another Method

def sum_elements_2 (lst) :
    result = 0

    for num in lst :
        result += num


    return result



print (sum_elements_2 ([1, 2, 3, 4, 5]))