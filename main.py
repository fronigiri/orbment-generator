from quartz import quartz_list
from characters import characters
from skills import skill_list, get_skills, print_skill_list





def main():
    print("======ORBMENT GENERATOR======")

    print("[1] Joshua")
    print("[2] Estelle")
    print("[3] Scherazard")
    print("[4] Agate")
    print("[5] Kloe")
    print("[6] Olivier")
    print("[7] Tita")
    print("[8] Zin")
    character_input = input("Please enter a number to select a character:")
    character = character_selector(character_input)
    slot_quartz(character)
    print("All quartz sloted!")
    print("Generating skill list...")
    skills = get_skills(character, skill_list)
    print_skill_list(skills)
    print("Skill list generated!")



def slot_quartz(character):
    for i in range(0, 5):
        if i + 1 in character.restricted_slots:
            name = input(f"Slot {i + 1} is a {character.element} slot. Please provide a valid quartz:")
            name_lower = name.lower()
            if name_lower not in quartz_list:
                raise Exception("Invalid quartz provided.")
            
            quartz = quartz_list[name_lower]

            if quartz.element != character.element:
                raise Exception("Incorrect element provided.")
            if quartz in character.quartz:
                raise Exception("The provided quartz is already sloted")
            character.quartz.append(quartz)
        else:
            name = input(f"Please provide quartz for slot {i + 1}:")
            name_lower = name.lower()
            if name_lower not in quartz_list:
                raise Exception("Invalid quartz provided.")
            
            quartz = quartz_list[name_lower]           
            if quartz in character.quartz:
                raise Exception("The provided quartz is already sloted")
            character.quartz.append(quartz)            


def character_selector(number):
    try:
        num_key = int(number)
    except ValueError:
        raise Exception("Error: Input is not a valid integer")
    char_map = {
        1: "joshua",
        2: "estelle",
        3: "scherazard",
        4: "agate",
        5: "kloe",
        6: "olivier",
        7: "tita",
        8: "zin",
    }
    if num_key in char_map:
        selected_char_key = char_map[num_key]
        print(f"Selected {characters[selected_char_key].name}")
        return characters[selected_char_key]
    else:
        raise Exception("Error: Please provide a valid number")
    


if __name__ == "__main__":
    main()