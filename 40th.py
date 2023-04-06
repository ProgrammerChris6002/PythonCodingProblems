def get_square_lst():
    lst = [i*i for i in range(1,21)]
    return lst[5:]

print (get_square_lst())



# Another Solution


def printList():
    li = list()
    for i in range(1,21):
        li.append(i**2)
    print(li[5:])

printList()
