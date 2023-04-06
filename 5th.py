class GetPrint ():
    def __init__ (self, string):
        self.string = string

    def getString (self):
        self.string = input ("Enter your string\n==> ")

    def printString (self):
        return self.string.upper ()


GP = GetPrint ('Ebuka')
GP.getString ()
print (GP.printString ())




# Another Solution



class InputOutString (object):
    def __init__ (self):
        self.s = ""

    def _getString (self):
        self.s = input ("Enter your string: ")

    def printString (self):
        print (self.s.upper ())


strObj = InputOutString ()
strObj._getString ()
strObj.printString ()