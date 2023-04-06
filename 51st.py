class American:
    pass

class NewYorker(American):
    pass


USA = American()
NewYork = NewYorker()




# Another Solution



class American(object):
    pass

class NewYorker(American):
    pass


anAmerican = American()
aNewYorker = NewYorker()

print(anAmerican)
print(aNewYorker)