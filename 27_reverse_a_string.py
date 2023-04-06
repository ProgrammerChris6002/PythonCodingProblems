def reverse_str (txt) :
    result = txt[::-1]

    return result


print (reverse_str ('Hello World.'))




# Another Solution



def reverse_string (str) :
    reverse = ""

    for char in str :
        reverse = char + reverse


    return reverse



str = input ("Enter your string: ")

result = reverse_str (str)
print (result)