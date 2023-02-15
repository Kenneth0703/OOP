import random

class Bug:

    def __init__(self,n,w,l):
        self.name = n
        self.flight = 0
        self.wings = w 
        self.legs = l

    def fly(self):
        self.flight = random.randint(0,10)
        
    def get_flight(self):
        return self.flight

    def get_name(self):
        return self.name
