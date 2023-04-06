def palindrome_word (word) :
    str = ''

    word_lst = list (word)
    word_lst.reverse ()
    
    for words in word_lst :
        str += words


    if (word == str) :
        result = f'\'{word}\' is a palindrome!'
        return result
    else :
        result = f'\'{word}\' is not a palindrome!'
        return result



print (palindrome_word ('ebuka'))
print (palindrome_word ('rotor'))
print (palindrome_word ('kayak'))
print (palindrome_word ('word'))
print (palindrome_word ('level'))
print (palindrome_word ('madam'))
print (palindrome_word ('racecar'))




# Another Solution



my_str = input ('String to check: ')

rev_str = my_str[::-1]


if (my_str == rev_str) :
    print ("It is a palindrome")
else :
    print ("It is not a palindrome")