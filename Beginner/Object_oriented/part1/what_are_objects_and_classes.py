

#The class keyword lets us define a class. We use it just like we do the def keyword for making functions.
#Class definitions are blocks like function definitions.

#class NewClass:

#Inside of the class, variables are called attributes.

class NewClass:
    name_attribute = "Kenneth"

#And functions that are defined inside of a class are called methods.

class NewClass:
    name_attribute = "Kenneth"

    def name_method(self):
        return self.name_method

#Whenever we call a class, it creates an instance. 
#Each instance has full access to the all of the attributes and methods of the class.

new_instance = NewClass()
new_instance.name_method()

#exmple from video

class Thief:
    sneaky = True

    def pickpocket(instance):
        if instance.sneaky:
            return bool(random.randint(0, 1))
        return False


