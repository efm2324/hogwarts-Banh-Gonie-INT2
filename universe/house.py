import sys
from pathlib import Path

# Add the parent directory to sys.path so we can import utils (doesn't work without this)
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.input_utils import load_file
from utils.input_utils import init_character

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
        
def assign_house(questions, houses):
    for question, options, house_mapping in questions:
        print("\n" + question)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        while True:
            try:
                choice = int(input("Your choice: "))
                if 1 <= choice <= 4:
                    selected_house = house_mapping[choice - 1]
                    houses[selected_house] += 1
                    break
                else:
                    print("Please select a valid option.")
            except ValueError:
                print("Please enter a number between 1 and 4.")
    
    display_winning_house(houses)


