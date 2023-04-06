def word_frequency (sentence):
    dct = dict ()
    lst = sentence.split (' ')
    lst.sort ()
    lst_2 = []
    result = ''

    for i in lst:
        if (i not in dct):
            dct[i] = 1
        elif (i in dct):
            dct[i] += 1

    for keys, values in dct.items ():
        temp_lst = [str (keys), str (values)]
        var = ':'.join (temp_lst)
        lst_2.append (var)
    result += ' '.join (lst_2)
        
    return result

sentence = input ("Enter your sentence\n==> ")
print (word_frequency (sentence))




# Another Solution



freq = {} # frequency of words in text
line = input ("Enter your sentence: ")

for word in line.split ():
    freq[word] = freq.get (word, 0)+1

words = list(freq.keys ())
words.sort ()

for w in words:
    print ("%s:%d" % (w, freq[w]))