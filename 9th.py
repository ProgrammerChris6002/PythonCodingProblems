def upper_deco (function):
    def wrapper (string):
        func = function (string)
        uppercase = func.upper ()

        return uppercase
    return wrapper


@ upper_deco

def upper_txt (string):
    return string


string = input ("Enter your string\n==> ")
print (upper_txt (string))



lines = []


while True:
    s = input ("Enter your string: ")

    if (len(s) > 1):
        lines.append (s.upper ())
    else:
        break

for sentence in lines:
    print (sentence)