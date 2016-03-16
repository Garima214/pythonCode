# -*- coding: utf-8 -*-

class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        area = self.length * self.width
        print "Area of rectangle = %s" %area
        
rect = Rectangle(3,5)
rect.area()