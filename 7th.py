def gen_2d_array (xy):
    lst_two = xy.split (',')
    x = int (lst_two[0])
    y = int (lst_two[1])
    lst = []

    for i in range (x):
        lst.append ([(a*i) for a in range (y)])


    return lst



xy = input ("How many sub list(s) and element(s)\n==> ")
print (gen_2d_array (xy))





# Another Solution




input_str = input ("Enter the values: ")
dimensions = [int (x) for x in input_str.split (',')]
rowNum = dimensions[0]
colNum = dimensions[1]

multilist = [[0 for col in range (colNum)] for row in range (rowNum)]

for row in range (rowNum):
    for col in range (colNum):
        multilist[row][col] = row*col


print (multilist)