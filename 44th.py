def print_yes (sentence):
    if (sentence == "yes") or (sentence == "YES") or (sentence == "Yes"):
        print ("Yes")
    else:
        print ('No')

sentence = input ("Enter your sentence\n==> ")
print_yes (sentence)



# Another Solution


s = input ("Enter your sentence: ")

if (s == "yes") or (s =='YES') or (s == "Yes"):
    print ("Yes")
else:
    print ("No")