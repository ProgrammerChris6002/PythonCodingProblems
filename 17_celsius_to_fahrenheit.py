def cel_to_fah (celsius) :
    fahrenheit = (((celsius) * (9)) / (5) + (32))

    return f'{fahrenheit}F'


celsius = float (input ('Enter temperature in degrees Celsius: '))

print (cel_to_fah (celsius))