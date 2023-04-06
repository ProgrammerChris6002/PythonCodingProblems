def final () :
    


    def full_name (name):

        if name.isalpha() == True:
            print(f'Welcome, {name.capitalize ()}')
            return True
        elif name.isalpha() == False:
            while name.isalpha() == False:
                print(f'Name \'{name}\' is invalid')
                name = input('Firstname: ').strip().capitalize()
            else:
                print(f'Welcome, {name.capitalize ()}')
                return True

    full_name(name_2)     

    def how_old (age):

        if age.isdecimal() == True:
            print(f'You are {age} years old')
            return True
        elif age.isdecimal() == False:
            while age.isdecimal() == False:
                print(f'age \'{age}\' is invalid')
                age = input('Age: ').strip()
            else:
                print(f'You are {age} years old')
                return True

    how_old(age_2)

name_2 = input ('Enter name: ')
age_2 = input ('Enter age: ')

final ()