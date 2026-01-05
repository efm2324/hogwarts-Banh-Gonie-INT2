def init_character(last_name, first_name, attributes):

    return {
        "Last Name": str(last_name),
        "First Name": str(first_name),
        "House": None,      # Added this as Chapter 1 assigns a house
        "Money": 100,
        "Inventory": [],
        "Spells": [],
        "Attributes": attributes
    }

def display_character(character):
    
    print("\n--- CHARACTER PROFILE ---")
    print(f"Name: {character.get('First Name')} {character.get('Last Name')}")
    print(f"House: {character.get('House', 'Not yet sorted')}")
    print(f"Money: {character.get('Money', 0)} Galleons")
    print("Attributes:")
    attrs = character.get("Attributes", {})
    for attr, value in attrs.items():
        print(f"  - {attr}: {value}")

    inventory = character.get("Inventory", [])
    print(f"Inventory: {', '.join(inventory) if inventory else 'Empty'}")
    
    spells = character.get("Spells", [])
    print(f"Spells Learned: {', '.join(spells) if spells else 'None'}")
    print("-------------------------\n")

def modify_money(character, amount):

    character["Money"] += amount
    if character["Money"] < 0:
        character["Money"] = 0
    return character["Money"]

def add_item(character, category, item):

    if category not in ["Inventory", "Spells"]:
        print(f"Error: {category} is not a valid category.")
        return False

    current_list = character[category]
    if any(i.lower() == item.lower() for i in current_list):
        print(f"You already have {item}!")
        return False
    
    character[category].append(item)
    print(f"Added to {category}: {item}")
    return True