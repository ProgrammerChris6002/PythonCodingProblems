# import time, pyautogui

# time.sleep (3)
# print (pyautogui.position ()) # 159,356

# num = 24

# for i in range (5):
#     pyautogui.moveTo (152, 223, duration=0.4)
#     pyautogui.click ()
#     time.sleep (0.4)

#     pyautogui.typewrite (f"{num}th.py", 0.005)
#     pyautogui.press ('enter')
#     time.sleep (2)

#     num += 1



def sort_name_age_score (text):
    lst = text.split (' ')
    lst.sort ()
    lst_2 = []

    for i in lst:
        lst_2.append (tuple (i.split (',')))

    return lst_2


text = input ("Enter your string\n==> ")
print (sort_name_age_score (text))




from operator import itemgetter, attrgetter
# Another Solution



l = []


while True:
    s = input ('Enter your string: ')

    if not s:
        break
    l.append (tuple (s.split (",")))

print (sorted (l, key=itemgetter))