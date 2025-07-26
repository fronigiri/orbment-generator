class Quartz:
    name = ""
    earth = 0
    water = 0
    fire = 0
    wind = 0
    time = 0
    space = 0
    mirage = 0
    

    def __init__(self, name, earth, water, fire, wind, time, space, mirage):
        self.name, self.earth, self.water, self.fire, self.wind, self.time, self.space, 
        self.mirage = name, earth, water, fire, wind, time, space, mirage
    
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
        
    
        
       
        




