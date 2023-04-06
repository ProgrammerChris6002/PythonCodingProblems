class MyClass:
    def __init__ (self, upper):
        self.upper = upper

    def __str__ (self):
        return self.upper.upper ()
    

P = MyClass ('Uppercase')
print (P)




# Solution



class Person:
    # Define the class parameter "name"
    name = "Person"

    def __init__ (self, name = None):
        # self.name is the instance parameter
        self.name = name


jeffrey = Person ("Jeffrey")
print ("%s name is %s" % (Person.name, jeffrey.name))

nico = Person ()
nico.name = "Nico"
print ("%s name is %s" % (Person.name, nico.name))