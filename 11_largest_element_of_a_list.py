def largest_ele_lst (lst) :
    largest = lst[0]

    for i in lst :
        if (i > largest) :
            largest = i


    return largest



print (largest_ele_lst ([1, 2, 3, 7, 9, 4, 5]))




def largest_ele_lst_2 (lst) :
    result = max (lst)

    return result


print (largest_ele_lst_2 ([1, 4, 3, 7, 5]))