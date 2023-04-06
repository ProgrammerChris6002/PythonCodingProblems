# Equation Format :  a1x + b1y = c1   and   a2x + b2y = c2
print('Equation is in this format :  \n \t a1x + b1y = c1 \n \t a1x + b1y = c1')


def main():
    a1 = int(input('Enter a1: '))
    b1 = int(input('Enter b1: '))
    c1 = int(input('Enter c1: '))

    a2 = int(input('Enter a2: '))
    b2 = int(input('Enter b2: '))
    c2 = int(input('Enter c2: '))
    equation(a1, b1, c1, a2, b2, c2)


def equation(a1, b1, c1, a2, b2, c2):
        
    d = a1 - a2
    e = b1 - b2
    f = c1 - c2


    if a1 == a2:

        y = (f - d) / (e)
        x = ((c1 * e) - (b1 * f) + (b1 * d)) / (a1 * e)

    elif b1 == b2:
        x = (f - e) / (d)
        y = ((c1 * d) - (a1 * f) + (a1 * e)) / (b1 * d)

    elif a1 != a2 and b1 != b2:
        x = ((b2 * c1) - (b1 * c2)) / ((a1 * b2) - (a2 * b1))
        y = ((c2) - (a2 * x)) / (b2)

    print(f'\t x = {x} \n \t y = {y}')

main()