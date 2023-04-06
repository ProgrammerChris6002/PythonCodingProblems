def get_keys ():
    dct = dict ()
    for i in range (1,21):
        dct[i] = i*i
    for k in dct:
        print (k)

get_keys ()



# Another Solution


def printDict ():
    d = dict ()
    for i in range (1,21):
        d[i] = i ** 2
    for (k,v) in d.items ():
        print (v)

printDict ()