def get_tpl ():
    tpl = tuple([i*i for i in range(1,21)])
    return tpl

print (get_tpl ())



# Another Solution


def printTuple():
    li = list()
    for i in range(1,21):
        li.append(i**2)
    print(tuple(li))

printTuple()