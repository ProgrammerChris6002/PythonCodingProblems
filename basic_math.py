options = int(input('\n \t  1. Addition(+) \n \t  2. Subtraction(-) \n \t  3. Multiplication(*) \n \t  4. Division(/) \n \t  5. Exponentiation(e.g \u00B2)\n \t  6. Floor Division(//)\n \t  7. Modulus(%) \n \t  8. Simultaneous Equation(e.g   a1x + b1y = c1  and  a2x + b2y = c2) \n Enter Option :  '))
print(options)



if options == 1:
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    ans = f'{a} + {b} = {a + b}'
    print(ans)

elif options == 2:
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    ans = f'{a} - {b} = {a - b}'
    print(ans)

elif options == 3:
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    ans = f'{a} * {b} = {a * b}'
    print(ans)

elif options == 4:
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    ans = f'{a} / {b} = {a / b}'
    print(ans)

elif options == 5:
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    ans = f'{a}^{b} = {a ** b}'
    print(ans)

elif options == 6:
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    ans = f'{a} // {b} = {a // b}'
    print(ans)

elif options == 7:
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    ans = f'{a} * {b} = {a * b}'
    print(ans)

elif options == 8:
    from simultaneous_eli_sub_1 import main