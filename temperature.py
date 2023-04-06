# Temperature Converter
# Fahenheit to Celsius *(9/5)+32 # Celsius to Fahenheit * (5/9)-32


options = int(input('\n \t 1. Fahenheit to Celsius \n \t 2. Celsius to Fahenheit \n \t 3. Kelvin to Celsius \n \t 4. Celsius to Kelvin \n Pick any option: '))
print(options)


if options == 1:
    F = int(input('Enter value in Fahenheit: '))

    C = (F * (9 / 5) + 32)
    print('Answer in Celsius: ', f'{C}C')

elif options == 2:
    C = int(input('Enter value in Celsius: '))

    F = (C - 32) * (5 / 9)
    print('Answer in Fahenheit: ', f'{F}F')

elif options == 3:
    K = int(input('Enter value in Kelvin: '))

    C = K - 273
    print('Answer in Celsius is: ', f'{C}C')

elif options == 4:
    C = int(input('Enter value in Celsius: '))

    K = C + 273
    print('Answer in Kelvin is: ', f'{K}K')

else :
    print 