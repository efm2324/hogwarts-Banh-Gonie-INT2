import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.input_utils import ask_choice

houses = {
    "Gryffindor": 0,
    "Slytherin": 0,
    "Hufflepuff": 0,
    "Ravenclaw": 0
}

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

def update_house_points(house_dict, house_name, points):
    if house_name in house_dict:
        house_dict[house_name] += points
        return house_dict
    else:
        print("House not found.")
        return False

def display_winning_house(house_dict):
    max_pts = max(house_dict.values())
    winners = [h for h, p in house_dict.items() if p == max_pts]
    
    if len(winners) > 1:
        print(f"It's a tie! {', '.join(winners)} are tied with {max_pts} points!")
    else:
        print(f"The winning house is {winners[0]} with {max_pts} points!")

def assign_house(character, question_list):

    tally = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0}

    for q_text, choices, related_houses in question_list:
        user_choice_text = ask_choice(f"\n{q_text}", choices)

        choice_index = choices.index(user_choice_text)
        assigned_house = related_houses[choice_index]

        tally[assigned_house] += 1

    final_house = max(tally, key=tally.get)
    
    print(f"\nSorting Hat: 'Better be... {final_house.upper()}!'")
    return final_house