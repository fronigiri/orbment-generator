class Quartz:
    def __init__(self, name=0, earth=0, 
                 water=0, fire=0, wind=0, 
                 time=0, space=0, mirage=0, type=None, element=None):
        self.name = name
        self.earth = earth
        self.water = water
        self.fire = fire
        self.wind = wind
        self.time = time
        self.space = space
        self.mirage = mirage
        self.type = type
        self.element = element
    
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
        
    def __eq__(self, other):
        if isinstance(other, Quartz):
            return self.name == other.name
        return False

def line_total(line):
    total = {
        "fire": 0,
        "wind": 0,
        "time": 0,
        "water": 0,
        "mirage": 0,
        "space": 0,
        "earth": 0
    }
    for quartz in line:
        total["fire"] += quartz.get_sepith("fire")
        total["wind"] += quartz.get_sepith("wind")
        total["earth"] += quartz.get_sepith("earth")
        total["water"] += quartz.get_sepith("water")
        total["mirage"] += quartz.get_sepith("mirage")
        total["space"] += quartz.get_sepith("space")
        total["time"] += quartz.get_sepith("time")
    return total


#Earth Quartz
def_1 = Quartz("Defense 1", earth=1, type="def", element="earth")
def_2 = Quartz("Defense 2", earth=3, type="def", element="earth")
def_3 = Quartz("Defense 3", earth=5, type="def", element="earth")
poison = Quartz("Poison", earth=5, element="earth")
mute = Quartz("Mute", earth=3, element="earth")
petrify = Quartz("Petrify", earth=3, element="earth")

#Water Quartz
hp_1 = Quartz("HP 1", water=1, type="hp", element="water")
hp_2 = Quartz("HP 2", water=3, type="hp", element="water")
hp_3 = Quartz("HP 3", water=5, type="hp", element="water")
mind_1 = Quartz("Mind 1", water=1, type="mind", element="water")
mind_2 = Quartz("Mind 2", water=3, type="mind", element="water")
mind_3 = Quartz("Mind 3", water=5, type="mind", element="water")
freeze = Quartz("Freeze", water=3, element="water")
heal = Quartz("Heal", water=3, time=2, element="water")

#Fire Quartz
attack_1 = Quartz("Attack 1", fire=1, type="attack", element="fire")
attack_2 = Quartz("Attack 2", fire=3, type="attack", element="fire")
attack_3 = Quartz("Attack 3", fire=5, type="attack", element="fire")
seal = Quartz("Seal", fire=3, element="fire")
confuse = Quartz("Confuse", fire=3, element="fire")
strike = Quartz("Strike", fire=3, element="fire")

#Wind Quartz
shield_1 = Quartz("Shield 1", wind=1, type="shield", element="wind")
shield_2 = Quartz("Shield 2", wind=3, type="shield", element="wind")
shield_3 = Quartz("Shield 3", wind=5, type="shield", element="wind")
evade_1 = Quartz("Evade 1", wind=1, type="evade", element="wind")
evade_2 = Quartz("Evade 2", wind=3, type="evade", element="wind")
evade_3 = Quartz("Evade 3", wind=5, type="evade", element="wind")
impede_1 = Quartz("Impede 1", wind=1, type="impede", element="wind")
impede_2 = Quartz("Impede 2", wind=3, type="impede", element="wind")
impede_3 = Quartz("Impede 3", wind=5, type="impede", element="wind")
sleep = Quartz("Sleep", wind=3, element="wind")
scent = Quartz("Scent", wind=3, space=2, element="wind")

#Time Quartz
action_1 = Quartz("Action 1", time=1, type="action", element="time")
action_2 = Quartz("Action 2", time=3, type="action", element="time")
action_3 = Quartz("Action 3", time=5, type="action", element="time")
blind = Quartz("Blind", time=3, element="time")
cast_1 = Quartz("Cast 1", time=1, type="cast", element="time")
cast_2 = Quartz("Cast 2", time=3, type="cast", element="time")
deathblow = Quartz("Deathblow 1", time=3, type="deathblow", element="time")
deathblow_2 = Quartz("Deathblow 2", type="deathblow", element="time")

#Space Quartz
move_1 = Quartz("Move 1", space=1, type="move", element="space")
move_2 = Quartz("Move 2", space=3, type="move", element="space")
move_3 = Quartz("Move 3", space=5, type="move", element="space")
ep_cut_1 = Quartz("EP Cut 1", space=2, time=1, mirage=1, type="ep_cut", element="space")
ep_cut_2 = Quartz("EP Cut 2", space=3, time=2, mirage=2, type="ep_cut", element="space")
ep_cut_3 = Quartz("EP Cut 3", space=5, time=3, mirage=3, type="ep_cut", element="space")
range_1 = Quartz("Range 1", space=3, element="space")
eagle_eye = Quartz("Eagle Eye", space=3, mirage=2, element="space")

#Mirage Quartz
ep_1 = Quartz("EP 1", mirage=2, time=1, space=1, type="ep", element="mirage")
ep_2 = Quartz("EP 2", mirage=3, time=2, space=2, type="ep", element="mirage")
ep_3 = Quartz("EP 3", mirage=5, time=3, space=3, type="ep", element="mirage")
hit_1 = Quartz("Hit 1", mirage=1, type="hit", element="mirage")
hit_2 = Quartz("Hit 2", mirage=3, type="hit", element="mirage")
hit_3 = Quartz("Hit 3", mirage=5, type="hit", element="mirage")
information = Quartz("Information", mirage=2, element="mirage")
haze = Quartz("Haze", mirage=3, earth=2, element="mirage")
cloak = Quartz("Cloak", mirage=3, fire=2, element="mirage")

quartz_list = {}
quartz_list["defense 1"] = def_1
quartz_list["defense 2"] = def_2
quartz_list["defense 3"] = def_3
quartz_list["poison"] = poison 
quartz_list["mute"] = mute
quartz_list["petrify"] = petrify

quartz_list["hp 1"] = hp_1
quartz_list["hp 2"] = hp_2
quartz_list["hp 3"] = hp_3
quartz_list["mind 1"] = mind_1
quartz_list["mind 2"] = mind_2
quartz_list["mind 3"] = mind_3
quartz_list["freeze"] = freeze
quartz_list["heal"] = heal

quartz_list["attack 1"] = attack_1
quartz_list["attack 2"] = attack_2
quartz_list["attack 3"] = attack_3
quartz_list["seal"] = seal
quartz_list["confuse"] = confuse
quartz_list["strike"] = strike

quartz_list["shield 1"] = shield_1
quartz_list["shield 2"] = shield_2
quartz_list["shield 3"] = shield_3
quartz_list["evade 1"] = evade_1
quartz_list["evade 2"] = evade_2
quartz_list["evade 3"] = evade_3
quartz_list["impede 1"] = impede_1
quartz_list["impede 2"] = impede_2
quartz_list["impede 3"] = impede_3
quartz_list["sleep"] = sleep
quartz_list["scent"] = scent

quartz_list["action 1"] = action_1
quartz_list["action 2"] = action_2
quartz_list["action 3"] = action_3
quartz_list["blind"] = blind
quartz_list["cast 1"] = cast_1
quartz_list["cast 2"] = cast_2
quartz_list["deathblow"] = deathblow
quartz_list["deathblow 2"] = deathblow_2

quartz_list["move 1"] = move_1
quartz_list["move 2"] = move_2
quartz_list["move 3"] = move_3
quartz_list["ep cut 1"] = ep_cut_1
quartz_list["ep cut 2"] = ep_cut_2
quartz_list["ep cut 3"] = ep_cut_3
quartz_list["range 1"] = range_1
quartz_list["eagle eye"] = eagle_eye

quartz_list["ep 1"] = ep_1
quartz_list["ep 2"] = ep_2
quartz_list["ep 3"] = ep_3
quartz_list["hit 1"] = hit_1
quartz_list["hit 2"] = hit_2
quartz_list["hit 3"] = hit_3
quartz_list["information"] = information
quartz_list["haze"] = haze
quartz_list["cloak"] = cloak







