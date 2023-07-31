class Vector2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def getCopy(self):
        return Vector2D(self.x,self.y)
    
    def __add__(self, otherVector):
        if not isinstance(otherVector,Vector2D):
            raise Exception("Can't add: {}. Is not a Vector2d".format(otherVector))

        return Vector2D(self.x + otherVector.x, self.y + otherVector.y)
    
    def __sub__(self, otherVector):
        if not isinstance(otherVector,Vector2D):
            raise Exception("Can't sub: {}. Is not a Vector2d".format(otherVector))

        return self + (otherVector * -1)

    def __mul__(self, element):
        if type(element) is int or type(element) is float:
            return Vector2D(self.x * element, self.y * element)
        
        if type(element) is Vector2D:
            return Vector2D(self.x * element.x, self.y * element.y)

    def __str__(self):
        return "(x: {}, y: {})".format(self.x,self.y)