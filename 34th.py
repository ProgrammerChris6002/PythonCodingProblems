def get_square_values ():
    dct = {}
    for i in range (1,21):
        dct[i] = i * i
    for keys, values in dct.items ():
        print (values)

get_square_values ()



# Another Solution


def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	print(d)

printDict()