def cal_a (a):
    one = a
    two = a+a
    three = a+a+a
    four = a+a+a+a

    result = int (one) + int (two) + int (three) + int (four)

    return result


a = input ("Enter an integer\n==> ")
print ('Answer = ' , cal_a (a))




# Another Solution



a = input ("Enter an integer: ")

n1 = int ("%s" % a)
n2 = int ("%s%s" % (a,a))
n3 = int ("%s%s%s" % (a,a,a))
n4 = int ("%s%s%s%s" % (a,a,a,a))

print (n1+n2+n3+n4)