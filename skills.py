from quartz import Quartz

class Skill(Quartz):
    def __init__(self=None, name=None, earth=None, 
                 water=None, fire=None, wind=None, 
                 time=None, space=None, mirage=None, description=None):
        super().__init__(name, earth, water, fire, wind, time, space, mirage)
        self.description = description
# Earth Skills
stone_hammer = Skill(name="Stone Hammer", earth=1, description="Drops a large boulder on enemies.")
earth_lance = Skill(name="Earth Lance", earth=5, description="A pointed blade shoots up from the ground.")
petrify_breath = Skill(name="Petrify Breath", earth=3, description="Blows petrifying gas on an enemy. [Petrify 20%]")
stone_impact = Skill(name="Stone Impact", earth=3, space=2, description="Drops a massive boulder on enemies.")
titanic_roar = Skill(name="Titanic Roar", earth=8, space=4, description="Creates a powerful localized earthquake" )
earth_guard = Skill(name="Earth Guard", earth=2, description="Forms a temporary earth shield. [Immunity]")
earth_wall = Skill(name="Earth Wall", earth=4, description="Forms a temporary earth shield perimeter. [Immunity]")
crest = Skill(name="Crest", earth=4, water=3, space=2, mirage=1, description="Temporarily grants protection from the earth. [DEF+25%]")

# Water Skills
aqua_bleed = Skill(name="Aqua Bleed", water=1, description="Shoots a heavy stream of water at enemies.")
blue_impact = Skill(name="Blue Impact", water=5, description="Blasts an enemy with highly pressurized water.")
diamond_dust = Skill(name="Diamond Dust", water=4, space=1, wind=2, description="Produces intense cold. [Freeze 20%]")
tear = Skill(name="Tear", water=1, description="Heals 200HP for an ally.")
teara = Skill(name="Teara", water=4, description="Heals 1000HP for an ally.")
tearal = Skill(name="Tearal", water=6, description="Heals 2000HP for an ally.")
la_tear = Skill(name="La Tear", water=2, space=1, description="Heals 200HP for allies in the area.")
la_teara = Skill(name="La Teara", water=5, space=2, description="Heals 1000HP for allies in the area.")
thelas = Skill(name="Thelas", water=4, earth=2, mirage=1, description="Revives and heals 100HP")
curia = Skill(name="Curia", water=4, mirage=2, description="Cures all abnormal status except K.O.")
la_curia = Skill(name="La Curia", water=8, mirage=4, space=2, description="Cures status of all allies in area except those K.O.ed.")

#Fire Skills
fire_bolt = Skill(name="Fire Bolt", fire=1, description="Shoots a flaming ball of fire")
flame_arrow = Skill(name="Flame Arrow", fire=3, description="Showers an enemy with searing flames.")
napalm_breath = Skill(name="Napalm Breath", fire=6, description="Crimson flames that erupt from below.")
fire_bolt_ex = Skill(name="Fire Bolt EX", fire=3, wind=1, space=1, description="Sends a wave of flmaing balls of fire.")
spiral_flare = Skill(name="Spiral Flare", fire=5, wind=2, space=2, description="A chaotic flurry of scorching arrows.")
volcanic_rave = Skill(name="Volcanic Rave", fire=8, earth=4, space=2, description="Causes an explosion of focused energy.")
forte = Skill(name="Forte", fire=4, wind=3, space=2, mirage=1, description="Temporarily boosts strength by fire. [STR+25%]")

#Wind Skills



