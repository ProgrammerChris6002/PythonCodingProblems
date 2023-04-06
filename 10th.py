def clean_space (function):
    def wrapper (string):
        func = function (string)
        lst = list (set (func.split (' ')))
        lst.sort ()

        clean = ' '.join (lst)

        return clean
    return wrapper


@ clean_space


def get_txt (string):
    return string

string = input ("Enter your string with space between them\n==> ")
print (get_txt (string))




# Another Solution



s = input ("Enter your string with space between them: " )

words = [word for word in s.split (" ")]

print (" ".join (sorted (list (set (words)))))