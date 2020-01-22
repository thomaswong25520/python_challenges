class Mister():
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Enter a string: ")

    def printString(self):
        return self.s.upper()

if __name__ == '__main__':
    m = Mister()
    m.getString()
    print(m.printString())
    
    
