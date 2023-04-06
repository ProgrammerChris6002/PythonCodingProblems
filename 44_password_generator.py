import string
import random

def gen_pass ():
    letters = string.ascii_letters
    digits = string.digits
    punc = string.punctuation

    pass_char = letters + digits + punc
    pass_len = int (input ('Enter the length of the password==> '))

    password = random.sample (pass_char, pass_len)

    result = f"Your generated password is: {''.join (password)}"


    return result



print (gen_pass ())





# Another Solution




def generate_password (size):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''

    for char in range (size):
        rand_char = random.choice (all_chars)
        password = password + rand_char
    

    return password



pass_len = int (input ('How many characters in your password? '))
new_password = generate_password (pass_len)

print ('Your new password: ', new_password)