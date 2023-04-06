def square_lst ():
    lst = [i*i for i in range(1,21)]
    return lst[15:]

print (square_lst ())



# Another Solution


def printList ():
    li = list()
    for i in range(1,21):
        li.append(i**2)
    print(li[:5])

printList()