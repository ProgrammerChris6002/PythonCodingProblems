def miles_to_kilometers (miles) :
    kilometers = (float (miles) * 1.609344)

    return kilometers


miles = input ('Enter distance in miles: ')

print (miles_to_kilometers (miles))