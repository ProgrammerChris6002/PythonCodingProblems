import math


def cal (D):
    C = 50
    H = 30
    lst = D.split (',')
    lst_two = list ()

    for i in lst:
        D = float (i)
        Q = round (math.sqrt ((2*C*D) / (H)))
        lst_two.append (str (Q))

    result = ','.join (lst_two)


    return result



D = input ("Enter the values of D in a comma seperated sequence\n==> ")
print (cal (D))





# Another Solution




c=50
h=30
value = []

items = [x for x in input ("Enter the values of D in a comma seperated sequence: ").split (',')]

for d in items:
    value.append (str (int (round (math.sqrt (2*c*float(d)/h)))))

print (','.join (value))