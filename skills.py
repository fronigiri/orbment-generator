from quartz import Quartz, line_total

class Skill(Quartz):
    def __init__(self, name=None, earth=0, 
                 water=0, fire=0, wind=0, 
                 time=0, space=0, mirage=0, description=None):
        super().__init__(name, earth, water, fire, wind, time, space, mirage)
        self.description = description
    
    def __eq__(self, other):
        if isinstance(other, Skill):
            return self.name == other.name
        return False


def get_skills(character, skill_list):
    skills_found = []
    lines = character.lines
    for line in lines:
        total = line_total(line)
        for skill in skill_list:
            if (skill.get_sepith("earth") > total["earth"] or
                skill.get_sepith("water") > total["water"] or
                skill.get_sepith("fire") > total["fire"] or
                skill.get_sepith("wind") > total["wind"] or
                skill.get_sepith("time") > total["time"] or
                skill.get_sepith("space") > total["space"] or
                skill.get_sepith("mirage") > total["mirage"]):
                continue
            if (skill in skills_found):
                continue
            skills_found.append(skill)
    return skills_found
def print_skill_list(list):
    print("==========Skill List==========")
    for skill in list:
        print(f"{skill.name}")
    print("==============================")

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
air_strike = Skill(name="Air Strike", wind=1, description="Tears and shreds an enemy with compressed air.")
aerial = Skill(name="Aerial", wind=4, description="A powerful tornado with whirling bits of rubble.")
aero_storm = Skill(name="Aero Storm", wind=8, description="Creates a massive vortex of slicing aero blades.")
lightning = Skill(name="Lightning", wind=4, space=2, description="Sends out an electrical shock. [Seal 20%]")
plasma_wave = Skill(name="Plasma Wave", wind=8, space=4, description="Strikes with electrical bolts. [Seal 20%]")
sylphen_guard = Skill(name="Sylphen Guard", wind=2, description="Creates a temporary wind barrier.[AGL+50%]")
sylphen_wing = Skill(name="Sylphen Wing", wind=6, description="Temporarily borrows the power of wind. [MOV+1]")

#Time Skills
shadow_spear = Skill(name="Shadow Spear", time=5, description="A blade that whittles away life. [K.O. 20%]")
hell_gate = Skill(name="Hell Gate", time=4, space=2, mirage=1, description="Stagnates enemies' vital activities. [Faint 20%]")
white_gehenna = Skill(name="White Gehenna", time=8, space=4, mirage=2, description="Disrupts the time-space continuum. [Faint 20%]")
soul_blur = Skill(name="Soul Blur", mirage=1, description="Emits a time-space shaking pulse. [Faint 20%]")
clock_up = Skill(name="Clock Up", description="Speeds up the flow fo time. [SPD+25%]")
clock_up_ex = Skill(name="Clock Up EX", time=9, description="Greatly speeds up the flow of time. [SPD+50%]")
anti_sept = Skill(name="Anti-Sept", time=3, description="Temporarily prevents the casting of arts. [Mute]")
anti_sept_all = Skill(name="Anti-Sept All", time=11, description="Temporarily prevents the casting of arts. [Mute]")

# Mirage Skills
saint = Skill(name="Saint", mirage=4, earth=3, fire=3, water=2, wind=2, space=2, description="Temporarily increases an ally's parameters. [STR&DEF+25%]")
chaos_brand = Skill(name="Chaos Brand", mirage=5, description="Muddles an enemy's cognitive abilities. [Confuse]")

skill_list = [stone_hammer, earth_lance, petrify_breath,stone_impact, titanic_roar, earth_guard, earth_wall, crest,
                aqua_bleed, blue_impact, diamond_dust, tear, teara, tearal, la_tear, la_teara, thelas, curia, la_curia,
                 fire_bolt, flame_arrow, napalm_breath, fire_bolt_ex, spiral_flare, volcanic_rave, forte, air_strike, 
                 aerial, aero_storm, lightning, plasma_wave, sylphen_guard, sylphen_wing, shadow_spear, hell_gate, 
                 white_gehenna, soul_blur, clock_up, clock_up_ex, anti_sept, anti_sept_all, saint, chaos_brand]
