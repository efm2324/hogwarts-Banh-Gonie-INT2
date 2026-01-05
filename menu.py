# menu.py
import sys
from utils.input_utils import ask_choice
from chapters.chapter_1 import start_chapter_1
from chapters.chapter_2 import start_chapter_2
from chapters.chapter_3 import start_chapter_3
from chapters.chapter_4 import start_chapter_4_quidditch
from chapters.chapter_5_extension import final_duel_basilisk 

def display_main_menu():

    houses = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }

    options = ["Start New Adventure", "Exit Game"]
    choice = ask_choice("Welcome to Hogwarts. Choose an option:", options)

    if choice == "Exit Game":
        print("\nFarewell, wizard. Your owl awaits your return.")
        sys.exit(0)

    if choice == "Start New Adventure":
        character = start_chapter_1()
        character = start_chapter_2(character)
        character = start_chapter_3(character, houses)

        print("\nMOVING TO THE QUIDDITCH PITCH")
        character = start_chapter_4_quidditch(character, houses)

        print("THE AIR GROWS COLD... SOMETHING IS WRONG.")
        print("A cold draft leads you to the girls' bathroom...")
        print("!"*50)

        victory = final_duel_basilisk(character, houses)

        if victory:
            print(" YOU HAVE WON THE HOUSE CUP AND SAVED HOGWARTS! ")
            print("\nFinal House Standings:")
            for house, score in houses.items():
                print(f"- {house}: {score} pts")
        else:
            print("\nGame Over. The Chamber of Secrets remained closed to you.")