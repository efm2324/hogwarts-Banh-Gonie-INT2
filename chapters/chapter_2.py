def meet_friends(character):
    """Simple encounters with Ron, Hermione and Draco that update attributes.

    The function uses only basic input, print and simple loops.
    It expects `character` to be a dict with an `Attributes` dict inside.
    Returns the updated character.
    """

    # Ron
    print(
        "\nYou board the Hogwarts Express. The train slowly departs northward... \nA red-haired boy enters your compartment, looking friendly. \n\nHi! I'm Ron Weasley. Mind if I sit with you?\n")
    while True:
        choice = input("1. Sure, have a seat!\n2. Sorry, I prefer to travel alone.\n\nYour choice: ").strip()
        if choice == "1":
            print("Ron smiles: — Awesome! You'll see, Hogwarts is amazing!")
            character['Attributes']['Loyalty'] = character['Attributes'].get('Loyalty', 0) + 1
            break
        if choice == "2":
            print("Ron looks disappointed but nods: — Oh, okay. Sorry for bothering you.")
            character['Attributes']['Ambition'] = character['Attributes'].get('Ambition', 0) + 1
            break
        print("Please enter 1 or 2.")

    # Hermione
    print("\nA girl enters next, already carrying a stack of books. \n— Hello, I'm Hermione Granger. Have you ever read 'A History of Magic'?\n")
    while True:
        choice = input("1. Yes, I love learning new things\n2. Uh… no, I prefer adventures over books.\n\nYour choice: ").strip()
        if choice == "1":
            print("Hermione smiles, impressed: — Oh, that's rare! You must be very clever!")
            character['Attributes']['Intelligence'] = character['Attributes'].get('Intelligence', 0) + 1
            break
        if choice == "2":
            print("Hermione looks a bit disappointed: — Well, I suppose not everyone enjoys reading.")
            character['Attributes']['Courage'] = character['Attributes'].get('Courage', 0) + 1
            break
        print("Please enter 1 or 2.")

    # Draco (3 options)
    print("\nI'm Draco Malfoy. It's best to choose your friends carefully from the start, don't you think?\n")
    while True:
        choice = input("1. Shake his hand politely.\n2. Ignore him completely.\n3. Respond with arrogance.\n\nYour choice: ").strip()
        if choice == "1":
            print("Draco nods approvingly: — Hmph, not bad.")
            character['Attributes']['Ambition'] = character['Attributes'].get('Ambition', 0) + 1
            break
        if choice == "2":
            print("Draco frowns, annoyed. — You'll regret that! ")
            character['Attributes']['Loyalty'] = character['Attributes'].get('Loyalty', 0) + 1
            break
        if choice == "3":
            print("Draco looks surprised as you stand your ground. — Is that so? You've got guts.")
            character['Attributes']['Courage'] = character['Attributes'].get('Courage', 0) + 1
            break
        print("Please enter 1, 2 or 3.")

    # Show attributes in a simple way
    print("\nYour choices already say a lot about your personality!\nYour updated attributes:")
    for name, value in character.get('Attributes', {}).items():
        print(name + ':', value)

    return character

def welcome_message():
    message = (
        "\nProfessor Albus Dumbledore rises and looks across the Great Hall, his eyes twinkling with warmth.\n"
        "He speaks with a gentle, welcoming tone:\n\n"
        "\"Welcome to Hogwarts!\" he says. "
        "This place will test you, teach you, and give you friends for life.\n\n"
        "Take a moment to read these words and let them sink in."
    )
    print(message)
    input("\nPress Enter when you are ready to continue...")