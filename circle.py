# -*- coding: utf-8 -*-

class Circle:
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        area = 3.14 * self.radius * self.radius
        print "Area of Circle = %s" %area
        
circle1 = Circle(5)
circle1.area()