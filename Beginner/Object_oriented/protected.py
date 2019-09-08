class Protected:
    __name = 'Security'
    
    def __method(self):
        return self.__name
      
instance = Protected()
print(dir(instance))

print(instance._Protected__method())