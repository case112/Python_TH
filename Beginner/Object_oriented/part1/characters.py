#methods are used by the instance, not the class

#Super lets us use the code from our superclass on demand even if we\re ovewritten suff in our subclasses
#in other words super() lets you run a parents cla'ss version of a method

import random

class Character():
    #if new instance is created of the class python looks for __init__, 
    #python will run that method on its own, we dont have to call it ourselves, 
    #it lets us control how class is made or initialized, any special parameters etc
    def __init__(self, name, **kwargs):
        self.name = name
        
        for key, value in kwargs.items():
            setattr(self, key, value)
            

class Thief(Character):
    sneaky = True
        
    #that allows the sneakyness to be changed    
    def __init__(self, name, sneaky=True, **kwargs):
        super().__init__(name, **kwargs)
        self.sneaky = sneaky
    
    #methods take at least one parameter, wich represents the instance that is using the method, by convention its SELF
    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))
       
    def hide(self, light_level):
        return self.sneaky and light_level < 10

#to run it
instance = Thief("Oskar", scars=None, favourite_weapon = 'Sword')

#turns sneaky false
#instance.sneaky=False

print(instance.pickpocket())
#basicly same thing
print(Thief.pickpocket(instance))

print(instance.hide(9))

print(instance.favourite_weapon)