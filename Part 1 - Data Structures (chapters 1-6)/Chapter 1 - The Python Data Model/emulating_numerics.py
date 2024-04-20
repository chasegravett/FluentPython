# Several special methods allow user objects to respond to operators (like + or -)
# This will be a class to represent two-dimensional vectors (Also known as Euclidian Vectors)

# There is a built-in complex type that can represent n-dimensional vectors but that will come later
# Ex. of 2d vector addition -> Vector(2, 4) + Vector(2, 1) = Vector(4, 5)

import math

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"  # Usingg the !r here forces the f string to format using the repr() method on it instead of the ususal str() conversion
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other_vec):
        x = self.x + other_vec.x
        y = self.y + other_vec.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)