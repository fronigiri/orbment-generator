class Quartz:
    def __init__(self=None, name=None, earth=None, 
                 water=None, fire=None, wind=None, 
                 time=None, space=None, mirage=None):
        self.name = name
        self.earth = earth
        self.water = water
        self.fire = fire
        self.wind = wind
        self.time = time
        self.space = space
        self.mirage = mirage
    
    def get_sepeth(self, element):
        if element == 'earth':
            return self.earth
        elif element == 'water':
            return self.water
        elif element == 'fire':
            return self.fire
        elif element == 'wind':
            return self.wind
        elif element == 'time':
            return self.time
        elif element == 'space':
            return self.space
        elif element == 'mirage':
            return self.mirage
        
    
        
       
        




