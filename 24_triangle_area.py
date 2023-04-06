import math

def tri_area (a, b, c) :
    s = ((a + b + c) / (2))

    area = math.sqrt (s * (s - a) * (s - b) * (s - c))


    return f'Area of triangle: {round (area, 3)}m\u00B2'



a = float (input ('Enter side one in (m): '))
b = float (input ('Enter side two in (m): '))
c = float (input ('Enter side three in (m): '))

print (tri_area (a, b, c))