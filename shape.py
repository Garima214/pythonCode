# -*- coding: utf-8 -*-

class Shape:
    
    area = 0
    
    def __init__(self, leng, width, shape):
        self.leng = leng
        self.width = width
        self.shape = shape
        
    def area(self):
        area = self.leng * self.width
        print "Area of %s = %s" %(self.shape, area)
        
                
class Square(Shape):
    
    def __init__(self, length):
        Shape.__init__(self, length, length, "Square")
        
    def area(self):
        areaSq = self.leng * self.leng
        print "Square Area = %s" %areaSq
        
rect = Shape(3,5, "Rectangle")
rect.area()
sq = Square(4)
sq.area()