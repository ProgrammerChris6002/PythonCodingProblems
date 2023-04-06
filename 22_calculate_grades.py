def cal_grades (sc_one, sc_two, sc_three, sc_four, sc_five) :
    average = ((sc_one + sc_two + sc_three + sc_four + sc_five) / (5))

    if (average > 100) :
        return f'Score \'{average}\' cannot be greater than 100!'

    elif (average >= 75) :
        return f'{average}: Grade A'

    elif (average >= 65) :
        return f'{average}: Grade B'

    elif (average >= 50) :
        return f'{average}: Grade C'

    elif (average >= 45) :
        return f'{average}: Grade D'

    elif (average >= 40) :
        return f'{average}: Grade E'

    elif (average >= 0) :
        return f'{average}: Grade F'




sc_one = int (input ('Enter first score: '))
sc_two = int (input ('Enter second score: '))
sc_three = int (input ('Enter third score: '))
sc_four = int (input ('Enter fourth score: '))
sc_five = int (input ('Enter fifth score: '))

print (cal_grades (sc_one, sc_two, sc_three, sc_four, sc_five))