import sys
from pathlib import Path

# Add the parent directory to sys.path so we can import utils (doesn't work without this)
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.input_utils import load_file

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
        ["Charge in without hesitation", "Look for the best strategy", "Rely on your friends", 
        "Analyze the problem"], 
        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"] 
    ) 
]

def update_house_points(houses, house_name, points):
    if house_name in houses:
        houses[house_name] += points
        return houses
    else :
        print("House not found.")
        return False

def display_winning_house(houses):
    max_points = max(houses.values())
    winning_houses = [house for house, points in houses.items() if points == max_points]
    
    if len(winning_houses) > 1:
        print(f"It's a tie! {', '.join(winning_houses)} are tied with {max_points} points!")
    else:
        print(f"The winning house is {winning_houses[0]} with {max_points} points!")



def assign_house(character, questions):
    """Ask the sorting questions and return the assigned house.

    `questions` is a list of tuples: (question_text, choices_list, houses_list)
    """
    # initialize tally
    tally = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0}

    for q_text, choices, houses in questions:
        print("\n" + q_text)
        for i, choice in enumerate(choices, 1):
            print(f"{i}. {choice}")

        # repeat until valid choice
        while True:
            answer = input("Your choice: ").strip()
            if not answer.isdigit():
                print("Please enter the number of your choice.")
                continue
            idx = int(answer)
            if idx < 1 or idx > len(choices):
                print("Invalid choice number. Try again.")
                continue
            chosen_house = houses[idx - 1]
            tally[chosen_house] = tally.get(chosen_house, 0) + 1
            break

    # determine the winner (simple tie-break: first in list)
    max_points = max(tally.values())
    winning_houses = [h for h, p in tally.items() if p == max_points]
    assigned_house = winning_houses[0]
    return assigned_house