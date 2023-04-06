def dec_to_bin (num) :
    bits = []

    while (num > 0) :
        bits.append (num % 2)
        num //= 2

    bits.reverse ()

    binary = ''

    for bit in bits :
        binary += str (bit)


    return binary



num = int (input ('Enter a decimal number: '))

print (dec_to_bin (num))