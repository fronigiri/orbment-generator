class Character:
    quartz = []
    
    def __init__(self, name=None, lines=None, restricted_slots=None, element=None):
        self.name = name
        self.lines = lines
        self.restrcited_slots = restricted_slots
        self.element = element
    
    def make_lines(self):
        if self.name == "Olivier" or self.name == "Kloe":
            return self.quartz
        
        lines = []

        if self.name == "Estelle":
            lines.append((self.quartz[0], self.quartz[1], self.quartz[2], self.quartz[3]))
            lines.append((self.quartz[0], self.quartz[4], self.quartz[5]))
            return lines
        elif self.name == "Joshua":
            lines.append((self.quartz[0], self.quartz[1], self.quartz[2], self.quartz[3], self.quartz[4]))
            lines.append((self.quartz[0], self.quartz[6]))
            return lines
        elif self.name == "Scherazard":
            lines.append((self.quartz[0], self.quartz[1]))
            lines.append((self.quartz[0], self.quartz[2], self.quartz[3], self.quartz[4], self.quartz[5]))
            return lines
        elif self.name == "Tita":
            lines.append((self.quartz[0], self.quartz[1]))
            lines.append((self.quartz[0], self.quartz[2], self.quartz[3], self.quartz[4]))
            lines.append((self.quartz[0], self.quartz[5]))
            return lines
        elif self.name == "Agate":
            lines.append((self.quartz[0], self.quartz[1], self.quartz[2]))
            lines.append((self.quartz[0], self.quartz[3]))
            lines.append((self.quartz[0], self.quartz[4], self.quartz[5]))
            return lines
        elif self.name == "Zin":
            lines.append((self.quartz[0], self.quartz[1], self.quartz[2]))
            lines.append((self.quartz[0], self.quartz[3]))
            lines.append((self.quartz[0], self.quartz[4]))
            lines.append((self.quartz[0], self.quartz[5]))
            return lines
        

            


            






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
