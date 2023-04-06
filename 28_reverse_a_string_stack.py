def reverse_stack (str) :
    # create an empty stack (list to use as a stack)
    stack = []

    # Push all charcters of string to stack
    for char in str :
        stack.append (char)

    # Pop all characters of a string
    # and add it to the rev
    rev = ''

    while (len (stack) > 0) :
        last = stack.pop ()
        rev = rev + last
        # print (last, rev)


    return rev



usr_str = input ('What is your string: ')
reverse = reverse_stack (usr_str)

print ('Reversed is: ', reverse)