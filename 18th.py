import re

def password_requirements (password):
    lower, upper, digits, symbols = r"[a-z]", r"[A-Z]", r"[0-9]", r"[$#@]"
    pass_min, pass_max = 6, 12

    lower_match = re.findall (lower, password)
    upper_match = re.findall (upper, password)
    digits_match = re.findall (digits, password)
    symbols_match = re.findall (symbols, password)

    if (len (lower_match)>=1) and (len (upper_match)>=1) and (len (digits_match)>=1) and (len(symbols_match)>=1) and (len (password)>=pass_min) and (len (password)<=pass_max):

        return True

    return False


password = input ("Enter the password(s) to be checked as comma seperated values\n==> ")
result = ','.join (list(filter (password_requirements, password.split (','))))

print (result)





# Another Solution




value = []

items = [x for x in input ("Enter your password(s): ").split (',')]


for p in items:
    if (len (p)<6) or (len (p)>12):
        continue
    else:
        pass

        if not re.search ("[a-z]", p):
            continue
        elif not re.search ("[0-9]", p):
            continue
        elif not re.search ("[A-Z]", p):
            continue
        elif not re.search ("[$#@]", p):
            continue
        elif re.search ("\s", p):
            continue
        else:
            pass

        value.append (p)

print (",".join (value))