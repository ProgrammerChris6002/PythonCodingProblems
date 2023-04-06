from datetime import datetime
from datetime import date
import time


def get_birthday ():
    date_str = input ("Enter your date of birth.\nFormat: DD/MM/YYYY/n==> ")
    
    try:
        birthday = datetime.strptime (date_str, "%d/%m/%Y")
    except TypeError:
        birthday = datetime(*(time.strptime (date_str, "%d/%m/%Y")[0:6]))

    year, month, day = birthday.year, birthday.month, birthday.day

    return [year, month, day]


def cal_age (birth_year, birth_month, birth_day):
    now = datetime.now ()
    current_year = now.year
    current_month = now.month
    current_day = now.day

    year = current_year - birth_year
    month = current_month - birth_month
    day = current_day - birth_day

    if (month < 0):
        year = year - 1
    if (day < 0):
        month = month - 1

    age = year

    return age



birthday = get_birthday ()
age = cal_age (*birthday)

print ("Your are", age, "years old.")





# Another Solution




def calulate_age (born):
    today = datetime.today ()
    days = (today - born).days
    age = days // 365

    return age


def get_user_birthday ():
    date_str = input ("Enter your birth date in DD/MM/YYYY: ")

    try:
        birthday = datetime.strptime (date_str, "%d/%m/%Y")
    except TypeError:
        birthday = datetime(*(time.strptime (date_str, "%d/%m/%Y")[0:6]))

    return birthday



birthday = get_user_birthday ()
age = calulate_age (birthday)
print ("Your age: ", age)