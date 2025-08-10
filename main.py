from quartz import quartz_list
from characters import characters
from skills import skill_list
import os





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
    character_input = input("Please enter a number to select a character: ")
    character = character_selector(character_input)





def slot_quartz(character):
    for i in range(0, 5):
        if i + 1 in character.restricted_slots:
            input = input(f"Slot {i + 1} is a {character.element} slot. Please provide a valid quartz:")
            try:
                quartz = quartz_list[quartz]
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
            
        
            

            


            

        


def character_selector(input):
    if input == 1:
        print(f"Selected {characters["joshua"].name}")
        return characters["joshua"]

    if input == 2:
        print(f"Selected {characters["estelle"].name}")
        return characters["estelle"]
    
    elif input == 3:
        print(f"Selected {characters["scherazard"].name}")
        return characters["scherazard"]
    
    if input == 4:
        print(f"Selected {characters["agate"].name}")
        return characters["agate"]
    
    if input == 5:
        print(f"Selected {characters["kloe"].name}")
        return characters["kloe"]
    
    if input == 6:
        print(f"Selected {characters["olivier"].name}")
        return characters["olivier"]
    
    if input == 7:
        print(f"Selected {characters["tita"].name}")
        return characters["tita"]
    
    if input == 8:
        print(f"Selected {characters["zin"].name}")
        return characters["zin"]
    
    
    raise Exception("Error: Please provide a valid number")
    
    






if __name__ == "__main__":
    main()