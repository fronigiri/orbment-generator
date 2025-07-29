from quartz import Quartz

class Skill(Quartz):
    def __init__(self=None, name=None, earth=None, 
                 water=None, fire=None, wind=None, 
                 time=None, space=None, mirage=None, description=None):
        super().__init__(name, earth, water, fire, wind, time, space, mirage)
        self.description = description

stone_hammer = Skill(name="Stone Hammer", earth=1, description="Drops a large boulder on enemies.")

