class RaceCar():
    
    def __init__(self, color='red', fuel_remaining=100, **kwargs):
        self.laps = 0
        self.color = color
        self.fuel_remaining = fuel_remaining
        
        for attribute, value in kwargs.items():
            setattr(self, attribute, value)
            
    def run_lap(self, length):
        self.fuel_remaining =  self.fuel_remaining - (length * 0.125)
        self.laps += 1
        