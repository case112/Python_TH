class Wheels():
    def __init__(self, color, fuel_remaining, **kwargs):
        self.laps = 0
        self.color = color
        self.fuel_remaining = fuel_remaining
        
        for attribute, value in kwargs.items():
            setattr(self, attribute, value)

class RaceCar(Wheels):
            
    def run_lap(self, length):
        self.fuel_remaining =  self.fuel_remaining - (length * 0.125)
        print(self.fuel_remaining)
        self.laps += 1
        