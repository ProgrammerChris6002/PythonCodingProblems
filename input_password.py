from getpass import getpass

password = getpass (prompt='Password: ',)
print (password)



import pwinput


password = pwinput.pwinput ()
print (password)

password = pwinput.pwinput (prompt='Password: ')
print (password)

password = pwinput.pwinput (mask='X')
print (password)

password = pwinput.pwinput (mask='')
print (password)