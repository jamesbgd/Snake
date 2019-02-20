
class Posn():

    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y
    
    def getX(self):
        return self.xCoord
    
    def getY(self):
        return self.yCoord
    
    def setX(self, x):
        self.xCoord = x
    
    def setY(self, y):
        self.yCoord = y

    def addCoord(self, x, y):
        self.xCoord += x
        self.yCoord += y