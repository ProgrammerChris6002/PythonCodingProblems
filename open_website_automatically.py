# Python program to create a website alarm

# Import the webbrowser and time module
import webbrowser
import time

# Taking website to be opened as input
link = input ("Enter the link to website you want to open-> ")

links = [
    'facebook.com',
    'google.com',
    'youtube.com'
]

# Taking alarm time from the user
alarm = input ("Set the website alarm time as (Format:- HH:MM:SS)(24 hour format)-> ")

# This is the actual time that we will use to print.
current_time = time.strftime ("%H:%M:%S")

# Printing current time until alarm time
while (current_time != alarm) :
    print ('Wating, the current time is ' + current_time + " :-( " )
    current_time = time.strftime ("%H:%M:%S")
    time.sleep (1)

# Opening the webpage at alarm time
if (current_time == alarm) :
    for url in links :
        print ('WEBSITE IS OPENED :D')
        webbrowser.open_new_tab (url)