# -*- coding: utf-8 -*-

class American:
    
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        
    def displayMembers(self):
        print "Name: %s" %self.name
        print "Age: %s" %self.age
        print "City: %s" %self.city

class NewYorker(American):
    
    def __init__(self, name, age):
       American.__init__(self, name, age, "New York")
        
    def displayNewYorkers(self):
        print "New yorkers: "
        print "Name: %s" %self.name
        print "Age: %s" %self.age
        
John = American("John", 25, "Washington")
John.displayMembers()

Mathew = NewYorker("Mathew", 30)
Mathew.displayNewYorkers()