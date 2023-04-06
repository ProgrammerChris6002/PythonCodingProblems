def get_evens (num):
    if (num%2 == 0):
        return True
    return False
    
lst = [1,2,3,4,5,6,7,8,9,10]
even_nums = filter(get_evens, lst)
print (list(even_nums))



# Another Solution


li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x%2==0, li)
print (list(evenNumbers))