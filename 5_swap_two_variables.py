def swap_variables (var1=5, var2=3) :
    print (var1, var2)

    temp = var1
    var1 = var2
    var2 = temp


    return f'{var1} {var2}'


print (swap_variables ())




# Shortcut



def swap_variables_2 (var1=7, var2=4) :
    print (var1, var2)

    # swap these two
    var1, var2 = var2, var1
    return f'{var1} {var2}'


print (swap_variables_2 ())




# Another Solution



def swap_variables_3 (var1 = 9, var2 = 2) :
    print (var1, var2)

    # swap these two
    var1 = var1 + var2
    var2 = var1 - var2
    var1 = var1 - var2


    return f'{var1} {var2}'


print (swap_variables_3 ())