def sort_string (string):
    lst = string.split (',')
    lst.sort ()

    result = ','.join (lst)


    return result



string = input ("Enter words in comma seperated sequence\n==> ")
print (sort_string (string))





# Another Solution



items = [x for x in input ("Enter your words: ").split (',')]
print (items)
items.sort ()

print (','.join (items))