from utils.input_utils import ask_choice
from universe.house import assign_house

def meet_friends(character):

    print("\nThe Hogwarts Express")
    print("The train slowly departs northward. You find a compartment...")

    ron_options = ["Sure, have a seat!", "Sorry, I prefer to travel alone."]
    ron_choice = ask_choice("Ron Weasley: 'Mind if I sit with you?'", ron_options)
    
    if "Sure" in ron_choice:
        print("Ron smiles: 'Awesome! You'll see, Hogwarts is amazing!'")
        character['Attributes']['Loyalty'] += 1
    else:
        print("Ron looks disappointed: 'Oh, okay. Sorry for bothering you.'")
        character['Attributes']['Ambition'] += 1

    hermione_options = ["Yes, I love learning!", "I prefer adventures over books."]
    hermione_choice = ask_choice("\nHermione: 'Have you ever read A History of Magic?'", hermione_options)
    
    if "love learning" in hermione_choice:
        print("Hermione smiles: 'Oh, that's rare! You must be very clever!'")
        character['Attributes']['Intelligence'] += 1
    else:
        print("Hermione: 'Well, I suppose not everyone enjoys reading.'")
        character['Attributes']['Courage'] += 1

    draco_options = ["Shake his hand politely", "Ignore him completely", "Respond with arrogance"]
    draco_choice = ask_choice("\nDraco: 'Choose your friends carefully. Don't you think?'", draco_options)
    
    if "Shake" in draco_choice:
        character['Attributes']['Ambition'] += 1
    elif "Ignore" in draco_choice:
        character['Attributes']['Loyalty'] += 1
    else:
        character['Attributes']['Courage'] += 1

    return character

def sorting_ceremony(character):

    print("\n--- The Sorting Ceremony ---")
    print("The Great Hall is magnificent. Professor McGonagall places the hat on your head...")

    questions = [ 
        ( 
            "You see a friend in danger. What do you do?", 
            ["Rush to help", "Think of a plan", "Seek help", "Stay calm and observe"], 
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"] 
        ), 
        ( 
            "Which trait describes you best?", 
            ["Brave and loyal", "Cunning and ambitious", "Patient and hardworking", "Intelligent and curious"], 
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"] 
        ), 
        ( 
            "When faced with a difficult challenge, you...", 
            ["Charge in without hesitation", "Look for the best strategy", "Rely on your friends", "Analyze the problem"], 
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"] 
        )
    ]

    assigned = assign_house(character, questions)
    character["House"] = assigned
    
    print(f"\nSorting Hat: 'Better be... {assigned.upper()}!'")
    return character

def welcome_message():
    print("\nProfessor Dumbledore rises: 'Welcome! Welcome to a new year at Hogwarts!'")
    input("Press Enter to continue to the feast...")

def start_chapter_2(character):
    
    print("\nCHAPTER 2: ARRIVAL AT HOGWARTS")
    character = meet_friends(character)
    character = sorting_ceremony(character)
    welcome_message()
    print("\nEnd of Chapter 2!")
    return character