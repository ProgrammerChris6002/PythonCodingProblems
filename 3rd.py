def gen_dct (num):
    lst = [(i, i*i) for i in range (1, num+1)]

    dct = dict (lst)


    return dct



num = int (input ('How many numbers\n==> '))
print (gen_dct (num))




# Another Solution



n = int (input ("How many numbers\n==> "))
d= dict ()

for i in range (1, n+1):
    d[i] = i*i

print (d)