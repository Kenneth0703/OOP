import random

class Bug:

    def __init__(self):
        self.flight = 8
        self.wings = 4 
        self.legs = 2

    def fly(self):
        if random.randint(1,11) == 1:
            self.flight = "Distance"
        
    def get_flight(self):
        return self.flight