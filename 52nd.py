import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        a = math.pi * (self.radius ** 2)
        return round(a, 3)


MyCircle = Circle(10)
AreaOfCircle = MyCircle.area()

print(AreaOfCircle)




# Another Solution



class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    

aCircle = Circle(2)
print(aCircle.area())