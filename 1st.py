def divisible_by_7 ():
    lst = []

    for i in range (2000, 3201):
        if (i%7 == 0) and (i%5 != 0):
            lst.append (str (i))

    line = ','.join (lst)


    return line



print (divisible_by_7 ())





# Another Solution



l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l))