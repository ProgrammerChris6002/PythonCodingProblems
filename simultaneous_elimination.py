def main():
    a1 = int(input('Enter a1: '))
    b1 = int(input('Enter b1: '))
    c1 = int(input('Enter c1: '))

    a2 = int(input('Enter a2: '))
    b2 = int(input('Enter b2: '))
    c2 = int(input('Enter c2: '))


    equation(a1, b1, c1, a2, b2, c2)



def equation(a1, b1, c1, a2, b2, c2):
    d = ((a1 * a2) - (a1 * a2))
    e = ((a2 * b1) - (a1 * b2))
    f = ((a2 * c1) - (a1 * c2))


    y = ((f - d) / (e))

    x = (((a2 * c1 * e) + (a2 * b1 * d) - (a2 * b1 * f)) / (a1 * a2 * e))


    print(f'\n x = {x} \n y = {y}')


main()