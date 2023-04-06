# import time, pyautogui

# time.sleep (3)
# print (pyautogui.position ()) # 154,357

# num = 101


# for i in range (10):
#     if (str(num).endswith ('1')):
#         pyautogui.moveTo (154, 357, duration=0.4)
#         pyautogui.click ()
#         time.sleep (0.4)

#         pyautogui.typewrite (f"{num}st.py", 0.005)
#         pyautogui.press ('enter')
#         time.sleep (2)
#         num += 1

#     elif (str(num).endswith ('2')):
#         pyautogui.moveTo (154, 357, duration=0.4)
#         pyautogui.click ()
#         time.sleep (0.4)

#         pyautogui.typewrite (f"{num}nd.py", 0.005)
#         pyautogui.press ('enter')
#         time.sleep (2)
#         num += 1

#     elif (str(num).endswith ('3')):
#         pyautogui.moveTo (154, 357, duration=0.4)
#         pyautogui.click ()
#         time.sleep (0.4)

#         pyautogui.typewrite (f"{num}rd.py", 0.005)
#         pyautogui.press ('enter')
#         time.sleep (2)
#         num += 1

#     else:
#         pyautogui.moveTo (154, 357, duration=0.4)
#         pyautogui.click ()
#         time.sleep (0.4)

#         pyautogui.typewrite (f"{num}th.py", 0.005)
#         pyautogui.press ('enter')
#         time.sleep (2)
#         num += 1




def div_by_7 (n):
    for i in range (0, n):
        if (i % 7 == 0):
            yield i

for num in div_by_7 (70):
    print (num)




# Another Solution



def putNumbers (n):
    i = 0

    while (i < n):
        j = i
        i = i + 1
        if (j % 7 == 0):
            yield j


for i in putNumbers (70):
    print (i)