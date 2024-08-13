'''
Instructions :
The goal is to create a class that represents a simple circle.
A Circle can be defined by either specifying the radius or the diameter.
The user can query the circle for either its radius or diameter.

Other abilities of a Circle instance:

Compute the circle’s area
Print the attributes of the circle - use a dunder method
Be able to add two circles together, and return a new circle with the new radius - use a dunder method
Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
Be able to put them in a list and sort them
Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles

'''


import math # just for pi

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None: # if we get radius, we use it
            self._radius = radius
        elif diameter is not None: # if we get diameter, we calculate radius
            self._radius = diameter / 2
        else: # otherwise we raise error
            raise ValueError("You must specify either the radius or the diameter")

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self): # if we get radius, we calculate diameter
        return self._radius * 2

    @property
    def area(self):
        return math.pi * (self._radius ** 2)
    
    ''' Double underscore methods with reseved names'''

    def __str__(self):
        return f"Circle with radius: {self.radius}, diameter: {self.diameter}, area: {self.area:.2f}"

    def __add__(self, other):
        if isinstance(other, Circle): # Check if other object is also a Circle instance
            return Circle(radius=self.radius + other.radius)
        return NotImplemented # Safe way not to raise error if other is not Circle

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.radius <= other.radius
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.radius >= other.radius
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Circle):
            return self.radius != other.radius
        return NotImplemented


circle1 = Circle(radius=5)
circle2 = Circle(diameter=10)
circle3 = circle1 + circle2

print(circle1)  # Output: Circle with radius: 5, diameter: 10, area: 78.54
print(circle2)  # Output: Circle with radius: 5.0, diameter: 10.0, area: 78.54
print(circle3)  # Output: Circle with radius: 10.0, diameter: 20.0, area: 314.16

print(circle1 == circle2)  # Output: True
print(circle1 > circle2)   # Output: False
print(circle3 > circle1)   # Output: True

circles = [circle1, circle2, circle3]

# We implemented __lt__, __gt__, __le__, __ge__, and __eq__ so Python know how to sort the list of instances of Circle
circles.sort()  
for c in circles:
    print(c)
# Output: Circle with radius: 5, diameter: 10, area: 78.54
#         Circle with radius: 5.0, diameter: 10.0, area: 78.54
#         Circle with radius: 10.0, diameter: 20.0, area: 314.16
