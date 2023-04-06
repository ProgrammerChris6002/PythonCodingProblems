def bank_account_balance (sentence):
    lst = sentence.split (' ')
    lst_D = list ()
    lst_W = []

    for i in range (len (lst)):
        if (lst[i] == 'D'):
            lst_D.append (int(lst[i+1]))
        if (lst[i] == 'W'):
            lst_W.append (int(lst[i+1]))

    D = sum (lst_D)
    W = sum (lst_W)

    result = D - W

    return result


sentence = input ("Enter your statement\n==> ")
print (bank_account_balance (sentence))




# Another Solution



netAmount = 0


while True:
    s = input ("Enter your statement: ")

    if not s:
        break
    values = s.split (' ')
    operation = values[0]
    amount = int (values[1])

    if (operation=="D"):
        netAmount += amount
    elif (operation=="W"):
        netAmount -= amount
    else:
        pass


print (netAmount)