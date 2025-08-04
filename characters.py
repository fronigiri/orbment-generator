from quartz import Quartz

class Character:
    quartz = []
    lines = []
    def __init__(self, name=None, line_number=None, restricted_slots=None, element=None):
        self.name = name
        self.line_number = line_number
        self.restrcited_slots = restricted_slots
        self.element = element

    def line_total(self, line):
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
            total["fire"] += quartz.get_sepeth("fire")
            total["wind"] += quartz.get_sepeth("wind")
            total["earth"] += quartz.get_sepeth("earth")
            total["water"] += quartz.get_sepeth("water")
            total["mirage"] += quartz.get_sepeth("mirage")
            total["space"] += quartz.get_sepeth("space")
            total["time"] += quartz.get_sepeth("time")
        return total



    
    def make_lines(self):
        if self.name == "Olivier" or self.name == "Kloe":
            self.lines.append((self.quartz[0], self.quartz[1], self.quartz[3], self.quartz[4],self.quartz[5]))
            return

        if self.name == "Estelle":
            self.lines.append((self.quartz[0], self.quartz[1], self.quartz[2], self.quartz[3]))
            self.lines.append((self.quartz[0], self.quartz[4], self.quartz[5]))
            return
        
        elif self.name == "Joshua":
            self.lines.append((self.quartz[0], self.quartz[1], self.quartz[2], self.quartz[3], self.quartz[4]))
            self.lines.append((self.quartz[0], self.quartz[6]))
            return
        
        elif self.name == "Scherazard":
            self.lines.append((self.quartz[0], self.quartz[1]))
            self.lines.append((self.quartz[0], self.quartz[2], self.quartz[3], self.quartz[4], self.quartz[5]))
            return
        
        elif self.name == "Tita":
            self.lines.append((self.quartz[0], self.quartz[1]))
            self.lines.append((self.quartz[0], self.quartz[2], self.quartz[3], self.quartz[4]))
            self.lines.append((self.quartz[0], self.quartz[5]))
            return
        
        elif self.name == "Agate":
            self.lines.append((self.quartz[0], self.quartz[1], self.quartz[2]))
            self.lines.append((self.quartz[0], self.quartz[3]))
            self.lines.append((self.quartz[0], self.quartz[4], self.quartz[5]))
            return
        
        elif self.name == "Zin":
            self.lines.append((self.quartz[0], self.quartz[1], self.quartz[2]))
            self.lines.append((self.quartz[0], self.quartz[3]))
            self.lines.append((self.quartz[0], self.quartz[4]))
            self.lines.append((self.quartz[0], self.quartz[5]))
            return
        

            


            






joshua = Character("Joshua", 2, (1,4), "time")
zin = Character("Zin", 4, (1), "earth")
kloe = Character("Kloe", 1, (1, 2, 4), "water")
agate = Character("Agate", 3, (1, 6), "fire")
tita = Character("Tita", 3, (1, 6), "space")
olivier = Character("Olivier", 1, None, None)
estelle = Character("Estelle", 2, None, None)
scherazard = Character("Scherazard", 2, (1, 5), "wind")

characters = {}
characters["joshua"] = joshua
characters["zin"] = zin
characters["kloe"] = kloe
characters["agate"] = agate
characters["tita"] = tita
characters["olivier"] = olivier
characters["estelle"] = estelle
characters["scherazard"] = scherazard
