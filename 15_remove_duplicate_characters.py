def rm_dup (string) :
    res_str = ''

    for items in string :
        if (items not in res_str) :
            res_str += items


    return res_str



string = input ('What is your string: ')

print (rm_dup (string))