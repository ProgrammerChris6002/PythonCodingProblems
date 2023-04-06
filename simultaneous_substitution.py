def main():
    a1 = int(input('Enter a1: '))
    b1 = int(input('Enter b1: '))
    c1 = int(input('Enter c1: '))

    a2 = int(input('Enter a2: '))
    b2 = int(input('Enter b2: '))
    c2 = int(input('Enter c2: '))


    equation(a1, b1, c1, a2, b2, c2)



def equation(a1, b1, c1, a2, b2, c2):
    x = ((b2 * c1) - (b1 * c2)) / ((a1 * b2) - (a2 * b1))
    y = ((c2) - (a2 * x)) / (b2)

    # x = ((b1 * c2) - (b2 * c1)) / ((a2 * b1) - (a1 * b2)) # does same thing as line 16, just different formula
    # y = ((c1) - (a1 * x)) / (b1) # does same thing as line 17, just different formula


    print(f'\n x = {x} \n y = {y}')


main()