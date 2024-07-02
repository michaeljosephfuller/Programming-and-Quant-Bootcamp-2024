'''Emulating numeric types
Example: vector class'''

# Start by writing tests:

# >>> v1 = Vector(4, 3)
# >>> v2 = Vector(3, 1)

# >>> v1 + v2
# Vector(7, 4)

# >>> 3 * v1
# Vector(12, 9) 

# >>> abs(v1)
# 5.0

from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __abs__(self):
        return hypot(self.x, self.y)
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
        '''
        NOTE: this implementation only allows v1 * 3. Writing 3 * v1 will NOT work.
        This can be fixed with the special method __rmul__, explored in Chapter 13.
        '''

    def __bool__(self):
        '''Return false if zero vector, true otherwise'''
        return bool(abs(self))
        '''
        NOTE: if __bool__ is not implemented, then __len__ is used to determine the output.
        If self.__len__() == 0, then self.__bool__() is False. 
        Otherwise self.__bool__() is True, even if __len__ is not defined.
        '''
        '''
        NOTE: A faster way of writing __bool__ here is
        return bool(self.x or self.y)
        as you avoid using abs, sqrt and squaring. But this way is less readable.
        We need to use bool(x or y) here, else (x or y) returns an object e.g. x if bool(x) is True. 
        '''
    

v1 = Vector(4, 3)
v2 = Vector(3, 1)

print(v1 + v2)
print(v1 * 3)
print(abs(v1))
print(bool(Vector(0,0)))

# Exercise: extend this to an n-dimensional vector
