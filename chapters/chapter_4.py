import sys
import random
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.input_utils import load_file, ask_choice
from universe.house import update_house_points

def create_team(house, team_data, is_player=False, player_name=None):

    players_list = team_data.get("players", [])
    chasers = [p for p in players_list if "(Chaser)" in p]
    beaters = [p for p in players_list if "(Beater)" in p]
    seeker = next((p for p in players_list if "(Seeker)" in p), "Unknown Seeker")
    keeper = next((p for p in players_list if "(Keeper)" in p), "Unknown Keeper")

    team = {
        "House": house,
        "Score": 0,
        "Seeker": player_name if is_player else seeker,
        "Chasers": chasers,
        "Beaters": beaters,
        "Keeper": keeper
    }
    return team

def attempt_goal(attacking_team, defending_team, bonus=0):

    print(f"\nThe {attacking_team['House']} Chasers are mounting an attack!")
    
    success_threshold = 5 + bonus
    
    if random.randint(1, 10) <= success_threshold:
        attacking_team["Score"] += 10
        print(f"GOAL! {attacking_team['House']} scores 10 points!")
    else:
        print(f"The {defending_team['House']} Keeper, {defending_team['Keeper']}, makes a brilliant save!")

def catch_golden_snitch(player_team, opponent_team):

    print(" THE GOLDEN SNITCH HAS BEEN SPOTTED! ")
    print(f"{player_team['Seeker']} and {opponent_team['Seeker']} are in a dead heat!")

    winner = random.choice([player_team, opponent_team])
    winner["Score"] += 150
    
    print(f"\nUnbelievable! {winner['Seeker']} has caught the Snitch!")
    print(f"150 points awarded to {winner['House']}!")
    return True

def quidditch_match(character, houses):

    teams_data = load_file("data/teams_quidditch.json")
    if not teams_data:
        print("The match cannot proceed: Team data is missing.")
        return

    player_house = character.get("House", "Gryffindor")

    available_opponents = [h for h in teams_data.keys() if h != player_house]
    opponent_house = random.choice(available_opponents)
    
    full_name = f"{character.get('First Name', 'Student')} {character.get('Last Name', '')}"
    player_team = create_team(player_house, teams_data[player_house], is_player=True, player_name=full_name)
    opponent_team = create_team(opponent_house, teams_data[opponent_house])
    
    print(f"\nWelcome to the Quidditch Pitch: {player_house} vs {opponent_house}!")
    
    snitch_caught = False
    turn = 0

    while not snitch_caught and turn < 10:
        turn += 1
        print(f"\nTURN {turn}")
        print(f"Score: {player_team['House']} {player_team['Score']} - {opponent_team['Score']} {opponent_team['House']}")

        options = ["Aggressive Attack", "Tight Defense", "Search for Snitch"]
        strategy = ask_choice("Choose your team strategy:", options)

        if strategy == "Aggressive Attack":
            attempt_goal(player_team, opponent_team, bonus=2)
        elif strategy == "Tight Defense":
            print("You've commanded the beaters to protect the goals!")
            attempt_goal(opponent_team, player_team, bonus=-3)

        attempt_goal(opponent_team, player_team)

        if random.randint(1, 10) == 1:
            snitch_caught = catch_golden_snitch(player_team, opponent_team)

    print(f"FINAL SCORE: {player_team['House']} {player_team['Score']} - {opponent_team['Score']} {opponent_team['House']}")
    
    if player_team["Score"] > opponent_team["Score"]:
        print(f"VICTORY! {player_house} wins the match!")
        update_house_points(houses, player_house, 100)
    else:
        print(f"Defeat. {opponent_house} takes the win.")
        update_house_points(houses, opponent_house, 50)

def start_chapter_4_quidditch(character, houses):
    print(" CHAPTER 4: THE QUIDDITCH CUP ")

    quidditch_match(character, houses)
    
    print("\nThe crowd roars as the teams descend to the ground.")
    print("End of Chapter 4.")
    
    return character
