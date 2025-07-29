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
    
    def get_sepith(self, element):
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


#Earth Quartz
def_1 = Quartz("Defense 1", earth=1)
def_2 = Quartz("Defense 2", earth=3)
def_3 = Quartz("Defense 3", earth=5)
poison = Quartz("Poison", earth=5)
mute = Quartz("Mute", earth=3)
petrify = Quartz("Petrify", earth=3)

#Water Quartz
hp_1 = Quartz("HP 1", water=1)
hp_2 = Quartz("HP 2", water=3)
hp_3 = Quartz("HP 3", water=5)
mind_1 = Quartz("Mind 1", water=1)
mind_2 = Quartz("Mind 2", water=3)
mind_3 = Quartz("Mind 3", water=5)
freeze = Quartz("Freeze", water=3)
heal = Quartz("Heal", water=3, time=2)

#Fire Quartz
attack_1 = Quartz("Attack 1", fire=1)
attack_2 = Quartz("Attack 2", fire=3)
attack_3 = Quartz("Attack 3", fire=5)
seal = Quartz("Seal", fire=3)
confuse = Quartz("Confuse", fire=3)
strike = Quartz("Strike", fire=3)

#Wind Quartz
shield_1 = Quartz("Shield 1", wind=1)
shield_2 = Quartz("Shield 2", wind=3)
shield_3 = Quartz("Shield 3", wind=5)
evade_1 = Quartz("Evade 1", wind=1)
evade_2 = Quartz("Evade 2", wind=3)
evade_3 = Quartz("Evade 3", wind=5)
impede_1 = Quartz("Impede 1", wind=1)
impede_2 = Quartz("Impede 2", wind=3)
impede_3 = Quartz("Impede 3", wind=5)
sleep = Quartz("Sleep", wind=3)
scent = Quartz("Scent", wind=3, space=2)

#Time Quartz
action_1 = Quartz("Action 1", time=1)
action_2 = Quartz("Action 2", time=3)
action_3 = Quartz("Action 3", time=5)
blind = Quartz("Blind", time=3)
cast_1 = Quartz("Cast 1", time=1)
cast_2 = Quartz("Cast 2", time=3)
deathblow = Quartz("Deathblow 1", time=3)
deathblow_2 = Quartz("Deathblow 2")

#Space Quartz
move_1 = Quartz("Move 1", space=1)
move_2 = Quartz("Move 2", space=3)
move_3 = Quartz("Move 3", space=5)
ep_cut_1 = Quartz("EP Cut 1", space=2, time=1, mirage=1)
ep_cut_2 = Quartz("EP Cut 2", space=3, time=2, mirage=2)
ep_cut_3 = Quartz("EP Cut 3", space=5, time=3, mirage=3)
range_1 = Quartz("Range 1", space=3)
eagle_eye = Quartz("Eagle Eye", space=3, mirage=2)

#Mirage Quartz
ep_1 = Quartz("EP 1", mirage=2, time=1, space=1)
ep_2 = Quartz("EP 2", mirage=3, time=2, space=2)
ep_3 = Quartz("EP 3", mirage=5, time=3, space=3)
hit_1 = Quartz("Hit 1", mirage=1)
hit_2 = Quartz("Hit 2", mirage=3)
hit_3 = Quartz("Hit 3", mirage=5)
information = Quartz("Hit 3", mirage=2)
haze = Quartz("Haze", mirage=3, earth=2)
cloak = Quartz("Cloak", mirage=3, fire=2)


       
        




