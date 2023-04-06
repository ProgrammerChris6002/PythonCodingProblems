def even_nums ():
    lst = list ()
    for i in range (1000, 3001, 2):
        lst.append (str (i))
    
    result = ','.join (lst)

    return result


print (even_nums ())




# Another Solution



values = []


for i in range(1000, 3001):
    s = str(i)

    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
        
print(",".join(values))