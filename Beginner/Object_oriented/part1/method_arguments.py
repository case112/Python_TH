class Animal:
    #color = 'black'
    
    def __init__(self, color='grey', **kwargs):
        self.color = color
        
        for attribute, value in kwargs.items():
            setattr(self, attribute, value)
