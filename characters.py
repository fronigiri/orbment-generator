class Character:
    def __init__(self, name=None, lines=None, restricted_slots=None, element=None):
        self.name = name
        self.lines = lines
        self.restrcited_slots = restricted_slots
        self.element = element


joshua = Character("Joshua", 2, (1,4), "time")
zin = Character("Zin", 4, (1), "earth")
kloe = Character("Kloe", 1, (1, 2, 4), "water")
agate = Character("Agate", 3, (1, 6), "fire")
tita = Character("Tita", 3, (1, 6), "space")
olivier = Character("Olivier", 1, None, None)
estelle = Character("Estelle", 2, None, None)
scherazard = Character("Scherazard", 2, (1, 5), "wind")
