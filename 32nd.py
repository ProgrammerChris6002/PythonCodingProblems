def square_keys ():
    dct = dict ()
    for i in range (1, 4):
        dct[i] = i ** 2
    return dct

print (square_keys ())



# Another Solution


def printDict ():
    d= dict ()
    d[1] = 1 ** 2
    d[2] = 2 ** 2
    d[3] = 3 ** 2
    print (d)

printDict ()