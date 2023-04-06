from random import randint
from datetime import datetime
from datetime import date
import time


def time_to_birthday ():
    print ('Enter your next birthday.\nFormat: yyyy/mm/dd')

    bir_year = int (input ("Enter the year==> "))
    bir_month = int (input ("Enter the month==> "))
    bir_day = int (input ("Enter the day==> "))

    bir_inp = date (year=bir_year, month=bir_month, day=bir_day)

    now = date.today ()
    days_remaining = (bir_inp - now).days

    return f'Time remaining to birthday: {days_remaining} Days.'



print (time_to_birthday ())





# Another Solution




def get_user_birthday ():
    date_str = input ("Enter your birth date in DD/MM/YYYY: ")

    try:
        birthday = datetime.strptime (date_str, "%d/%m/%Y")
    except TypeError:
        birthday = datetime(*(time.strptime (date_str, "%d/%m/%Y")[0:6]))

    return birthday


def days_remaining (birth_date):
    now = datetime.now ()
    current_year = datetime (now.year, birth_date.month, birth_date.day)
    days = (current_year - now).days

    if (days < 0):
        next_year = datetime (now.year+1, birth_date.month, birth_date.day)
        days = (next_year - now).days

    return days



birthday = get_user_birthday ()
next_birthday = days_remaining (birthday)
print ("Your birthday is coming in: ", next_birthday)