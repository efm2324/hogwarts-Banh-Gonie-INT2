import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.input_utils import ask_number, ask_choice
from universe.character import init_character, display_character, modify_money, add_item

def introduction():
    print("\n*** WELCOME TO HOGWARTS ***")
    print("You are a young witch or wizard about to discover a world of magic.")
    input("\nPress Enter when you are ready to continue...")

def create_character():
    print("\nCharacter Creation")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    attributes = {
        "Courage": ask_number("Enter your Courage level (1-10): ", 1, 10),
        "Intelligence": ask_number("Enter your Intelligence level (1-10): ", 1, 10),
        "Loyalty": ask_number("Enter your Loyalty level (1-10): ", 1, 10),
        "Ambition": ask_number("Enter your Ambition level (1-10): ", 1, 10)
    }
    
    character = init_character(last_name, first_name, attributes)
    display_character(character)
    return character

def receive_letter():
    print("\nAn owl flies through the window, delivering a letter sealed with the Hogwarts crest...")
    print("“Dear Student, We are pleased to inform you that you have been accepted...”")

    options = ["Yes, of course!", "No, I'd rather stay with Uncle Vernon..."]
    choice = ask_choice("Do you accept this invitation?", options)
    
    if "No" in choice:
        print("\nYou have declined the invitation. The adventure ends here.")
        sys.exit(0)
    print("\nYou have accepted! Pack your bags.")

def meet_hagrid(character):
    print("\nA giant of a man approaches you: 'I'm Hagrid, Keeper of Keys and Grounds!'")
    options = ["Go with Hagrid", "Refuse"]
    choice = ask_choice("Will you follow him to Diagon Alley?", options)
    
    if "Refuse" in choice:
        print("'Blimey,' says Hagrid. He picks you up anyway. 'No time for that!'")
    else:
        print("Hagrid smiles. 'Right then, let's go!'")

def buy_supplies(character):
    print("\n Welcome to Diagon Alley ")
    
    required_items = ["Magic Wand", "Wizard Robe", "Potions Book"] 

    for item in required_items:
        print(f"\nYou need to buy: {item}")
        print(f"Current Gold: {character['Money']} Galleons")
        input(f"Press Enter to purchase {item} for 10 Galleons...")
        
        modify_money(character, -10)
        add_item(character, "Inventory", item)

    print("\nAll required items purchased! Time for a pet.")
    pets = ["Owl", "Cat", "Rat", "Toad"]
    pet_prices = {"Owl": 20, "Cat": 15, "Rat": 10, "Toad": 5}
    
    chosen_pet = ask_choice("Which pet do you want?", pets)
    price = pet_prices[chosen_pet]
    
    modify_money(character, -price)
    add_item(character, "Inventory", chosen_pet)

def start_chapter_1():
    introduction()
    character = create_character()
    receive_letter()
    meet_hagrid(character)
    buy_supplies(character)
    print("\nEnd of Chapter 1! You are ready for the Hogwarts Express.")
    return character