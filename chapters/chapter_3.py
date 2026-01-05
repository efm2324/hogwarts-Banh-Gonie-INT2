import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.input_utils import load_file, ask_choice
from universe.house import update_house_points
from universe.character import add_item

def learn_spells(character, file_path="data/spells.json"):
    print("\nTHE MAGIC CLASSROOM")
    print("Professor Flitwick: 'Swish and flick, everyone!'")
    
    all_spells = load_file(file_path)
    if not all_spells:
        print("Error: Could not load spells database.")
        return

    requirements = {
        "Offensive": 1,
        "Defensive": 1,
        "Utility": 3
    }
    
    total_to_learn = 5
    learned_count = 0

    while learned_count < total_to_learn:
        available_pool = [
            s for s in all_spells 
            if requirements.get(s['type'], 0) > 0 and s['name'] not in character['Spells']
        ]

        if not available_pool:
            available_pool = [s for s in all_spells if s['name'] not in character['Spells']]

        if available_pool:
            chosen_spell = random.choice(available_pool)
            add_item(character, "Spells", chosen_spell['name'])
            
            if chosen_spell['type'] in requirements:
                requirements[chosen_spell['type']] -= 1
            
            learned_count += 1
            print(f"Mastered: {chosen_spell['name']} [{chosen_spell['type']}]")
        else:
            break

    print("\nYour current Spellbook:")
    for spell_name in character['Spells']:
        print(f" - {spell_name}")

import random

def magic_quiz(character, houses, file_path="data/magic_quiz.json"):
    print("\n--- PROFESSOR SNAPE'S QUIZ ---")
    print(f"Snape: 'Let's see if you have anything in that head of yours, {character.get('First Name', 'Student')}...'")

    quiz_data = load_file(file_path)
    if not quiz_data:
        print("Snape: 'The quiz papers are missing. Five points from Gryffindor!'")
        return

    random.shuffle(quiz_data)
    
    score = 0
    for item in quiz_data[:5]:
        question = item['question']
        correct_answer = item['answer']

        other_answers = [q['answer'] for q in quiz_data if q['answer'] != correct_answer]
        wrong_choices = random.sample(other_answers, 3)

        options = [correct_answer] + wrong_choices
        random.shuffle(options)

        print(f"\nQuestion: {question}")
        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt}")

        while True:
            user_input = input("Your choice (number): ").strip()
            
            if not user_input.isdigit():
                print("Snape: 'Enter a number, dunderhead.'")
                continue
            
            choice_idx = int(user_input)
            if 1 <= choice_idx <= len(options):
                selected_text = options[choice_idx - 1]
                break
            else:
                print(f"Snape: 'Choose a number between 1 and {len(options)}.'")

        if selected_text == correct_answer:
            print("Snape: '...Correct. Unexpected.'")
            score += 1
        else:
            print(f"Snape: 'Wrong. The correct answer was: {correct_answer}.'")

    points_awarded = score * 10
    house_name = character.get("House")
    
    print(f"\nQuiz Finished! Result: {score}/5")

    if house_name and house_name in houses:
        houses[house_name] += points_awarded
        print(f"{points_awarded} points awarded to {house_name}!")

def start_chapter_3(character, houses):
    print("\nCHAPTER 3: LESSONS AND EXAMS")
    learn_spells(character)
    magic_quiz(character, houses)
    print("\nEnd of Chapter 3! You have survived your first semester.")
    return character