def dec_to_bin(dec_num):
    bits_lst = []
    while (dec_num > 0):
        bits_lst.append(dec_num % 2)
        dec_num = dec_num // 2
    bits_lst.reverse()
    bits_str = ""

    for i in bits_lst:
        bits_str += str(i)

    return bits_str

dec_num = int(input("Enter your decimal number\n==> "))
print(dec_to_bin(dec_num))