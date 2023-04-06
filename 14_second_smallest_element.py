def second_smallest (lst) :
    lst.remove (min (lst))

    sec_smallest = min (lst)


    return sec_smallest



print (second_smallest ([43, 83, 26, 26, 62, 23, 29]))




# Another Solution



def second_smallest_2 (lst) :
    smallest = lst[0]
    sec_smallest = lst[0]

    for i in range (len (lst)) :
        if (lst[i] < smallest) :
            sec_smallest = smallest
            smallest = lst[i]
        elif (lst[i] < sec_smallest) :
            sec_smallest = lst[i]


    return sec_smallest



print (second_smallest_2 ([43, 83, 26, 26, 62, 23, 29]))