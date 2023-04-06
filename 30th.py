def check_str (sentence1, sentence2):
    if (len (sentence1) > len (sentence2)):
        return f'Longest = {sentence1}'
    elif (len (sentence2) > len (sentence1)):
        return f'Longest = {sentence2}'
    else:
        return f'{sentence1}\n{sentence2}'
    
sentence1 = input ("Enter first string\n==> ")
sentence2 = input ("Enter second string\n==> ")
print (check_str (sentence1, sentence2))



# Another Solution


def printValue (s1,s2):
    len1 = len (s1)
    len2 = len (s2)

    if (len1 > len2):
        print (s1)
    elif (len2 > len1):
        print (s2)
    else:
        print (s1)
        print (s2)


printValue ("one", "three")