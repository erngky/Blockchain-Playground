# Define the class Point that has:

# Two attributes, x and y - the coordinates of the point on the plane;
# A constructor that accepts two arguments, x and y, that initialize the corresponding attributes. These arguments should have default value of 0.0;
# A method distance_to_origin() that returns the distance from the point to the origin. The formula for that is .
# A method reflect(), that reflects the point with respect to the x- or y-axis:
# accepts one argument axis,
# if axis="x" , it sets the y (not a typo!) attribute to the negative value of the y attribute,
# if axis="y", it sets the x attribute to the negative value of the x attribute,
# for any other value of axis, prints an error message.


import math
import numpy as np

class Point:
    """ A point on a 2D plane
    
   Attributes
    ----------
    x : float, default 0.0. The x coordinate of the point        
    y : float, default 0.0. The y coordinate of the point
    """
    def __init__(self, x=0.0, y=0.0):
      self.x = x
      self.y = y
      
    def distance_to_origin(self):
      """Calculate distance from the point to the origin (0,0)"""
      return np.sqrt(self.x ** 2 + self.y ** 2)
    
    def reflect(self, axis):
      """Reflect the point with respect to x or y axis."""
      if axis == "x":
        self.y = - self.y
      elif axis == "y":
        self.x = - self.x
      else:
        print("The argument axis only accepts values 'x' and 'y'!")

# """Test"""

# pt = Point(x=3.0)
# pt.reflect("y")
# print((pt.x, pt.y))
# pt.y = 4.0
# print(pt.distance_to_origin())

# """Output"""
# (-3.0,0.0)
# 5.0