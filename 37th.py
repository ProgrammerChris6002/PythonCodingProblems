def square_lst ():
    lst = [i*i for i in range(1,21)]
    lst_2 = list ()
    for i in range(5):
        lst_2.append(lst[i])
    print (lst_2)

square_lst ()



# Another Solution


def printList ():
    li = list ()

    for i in range(1,21):
        li.append(i**2)

    print(li)


printList ()