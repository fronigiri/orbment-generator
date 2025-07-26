class Character:
    name = ""
    lines = 0
    restricted_slots = []
    element = ""

    def __init__(self, name, lines, restricted_slots, element):
        self.name = name
        self.lines = lines
        self.restrcited_slots = restricted_slots
        self.element = element
