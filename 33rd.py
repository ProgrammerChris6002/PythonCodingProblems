def square_keys ():
    dct = {}
    for i in range (1, 21):
        dct[i] = i * i
    return dct

print (square_keys ())



# Another Solution


def printDict ():
    d = dict ()
    for i in range (1,21):
        d[i] = i ** 2
    print (d)

printDict ()