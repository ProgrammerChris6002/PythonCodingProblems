def upper_lower (sentence):
    dct = {"UPPERCASE":0, "LOWERCASE":0}

    for letter in sentence:
        if (letter.islower ()):
            dct["LOWERCASE"] += 1
        elif (letter.isupper ()):
            dct["UPPERCASE"] += 1

    return f"UPPERCASE {dct['UPPERCASE']} LOWERCASE {dct['LOWERCASE']}"


sentence = input ("Enter your sentence\n==> ")
print (upper_lower (sentence))




# Another Solution
import string



def upper_lower_2 (sentence):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    upper_str = ''
    lower_str = ''
    
    for i in sentence:
        if (i in upper):
            upper_str += i
        elif (i in lower):
            lower_str += i

    return f"UPPERCASE {len (upper_str)} LOWERCASE {len(lower_str)}"


sentence = input ("Enter your sentence\n==> ")
print (upper_lower_2 (sentence))




# Another Solution



s = input ("Enter your string: ")
d = {"UPPERCASE":0, "LOWERCASE":0}

for c in s:
    if (c.isupper ()):
        d["UPPERCASE"] += 1
    elif (c.islower ()):
        d["LOWERCASE"] += 1
    else:
        pass


print ("UPPERCASE", d["UPPERCASE"])
print ("LOWERCASE", d["LOWERCASE"])