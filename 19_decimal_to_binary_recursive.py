def dec_to_bin_recur (num) :
    if (num > 1) :
        dec_to_bin_recur (num//2)

    print (num % 2, end = '')


num = int (input ("Enter a decimal number: "))

dec_to_bin_recur (num)