import string


def cal_let_dig (sentence):
    strin = ''
    digi = ''
    letters = string.ascii_letters
    digits = string.digits

    for i in sentence:
        if (i in letters):
            strin += i
        elif (i in digits):
            digi += i

    return (f'LETTERS {len(strin)} DIGITS {len (digi)}')


sentence = input ("Enter your sentence\n==> ")
print (cal_let_dig (sentence))




# Another Solution



s = input ('Enter your string: ')
d = {"DIGITS":0, "LETTERS":0}

for c in s:
    if (c.isdigit ()):
        d["DIGITS"] += 1
    elif (c.isalpha ()):
        d['LETTERS'] += 1
    else:
        pass


print ("LETTERS", d['LETTERS'])
print ("DIGITS", d['DIGITS'])