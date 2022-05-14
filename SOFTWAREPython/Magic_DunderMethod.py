#class with magic methids
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # dunder magic method
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    #representation method whenever calling the object constructor
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    ## call method whenever calling the object constructor
    def __call__(self):
        print ("This vector which called has {0} and {1}".format(self.x, self.y))

vector1 = Vector(10,20)
vector2 = Vector(30,40)
vector3 = vector1 + vector2

print(vector3.x , vector3.y)
print(vector3)
vector3()