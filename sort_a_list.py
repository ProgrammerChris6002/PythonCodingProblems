def sort_lst(text, order):
    lst = text.split(",")
    nums = []
    for i in lst:
        nums.append(int(i))

    if (order == 'asc'):
        nums.sort()
    elif (order == 'desc'):
        nums.sort(reverse=True)
    elif (order == 'none'):
        return nums
    else:
        return f"Wrong input!"
    
    return nums
    

text = input("Enter your list values in a comma seperated sequence\n==> ")
order = input("What order do you wish to sort the list\n1. 'asc' for ascending\n2. 'desc' for descending\n3. 'none' to get the original list\n==> ")
print(sort_lst(text, order))