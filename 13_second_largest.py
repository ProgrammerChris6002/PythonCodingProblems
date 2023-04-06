def sec_largest (lst) :
    lst.remove (max (lst))

    sec_large = max (lst)
    

    return sec_large



print (sec_largest ([4,11,83,29,25,76,8]))




# Another Solution


def sec_largest_2 (nums) :
    large = nums[0]
    sec_large = nums[0]

    for i in range (1, len (nums)) :
        if (nums[i] > large) :
            sec_large = large
            large = nums[i]
        elif (nums[i] > sec_large) :
            sec_large = nums[i]


    return sec_large



print (sec_largest_2 ([4,11,83,29,25,76,8]))