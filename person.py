# -*- coding: utf-8 -*-

class Person:
    
    def __init__(self, gender):
        self.gender = gender
        
    def getGender(self):
        print "Gender: %s" %self.gender
        
class Male(Person):
    
    def __init__(self):
        Person.__init__(self,"Male")
        
    def getGender(self):
        print "Gender: %s" %self.gender
    
    
class Female(Person):
    
    def __init__(self):
        Person.__init__(self, "Female")
        
    def getGender(self):
        print "Gender: %s" %self.gender
        
maria = Female()
maria.getGender()

mathew = Male()
mathew.getGender()
    