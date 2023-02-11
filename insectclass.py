import random

class Bug:

    def __init__(self):
        self.flight = 8
        self.wings = 4 
        self.legs = 2

    def fly(self):
        self.flight = random.randint(0,10)
        
    def get_flight(self):
        return self.flight
