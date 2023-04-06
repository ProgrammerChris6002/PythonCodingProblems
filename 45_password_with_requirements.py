import string
import random

def gen_pass ():
    upper, lower, digits, spe_char = string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation

    pass_char = upper + lower + digits + spe_char

    lst = [upper, lower, digits, spe_char]
    result = ''

    for i in range (len (lst)):
        result += ''.join (random.sample (lst[i], 1))

    pass_len = int  (input ('Enter the password length(Minimum of 4)==> '))

    if (pass_len >= 4):
        for i in range ((pass_len) - len (result)):
            result += random.choice (pass_char)
        return result
    else:
        return 'Something went wrong.'


print (gen_pass ())





# Another Solution




def randomPassword (size):
    all_chars = string.ascii_letters + string.digits + string.punctuation

    password = ""
    password += random.choice (string.ascii_lowercase)
    password += random.choice (string.ascii_uppercase)
    password += random.choice (string.digits)
    password += random.choice (string.punctuation)

    for i in range (size-4):
        password += random.choice (all_chars)

    
    return password



pass_len = int (input ("What would be the password length? "))

print ("First Random Password is: ", randomPassword (pass_len))
print ("Second Random Password is: ", randomPassword (pass_len))
print ("Third Random Password is: ", randomPassword (pass_len))