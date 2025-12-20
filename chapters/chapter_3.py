import random
from utils.input_utils import load_file, ask_choice
from universe.house import update_house_points
from universe.character import add_item

def learn_spells(character, file_path="../data/spells.json"):

    print("\nYou begin your magic lessons at Hogwarts...")
    
    all_spells = load_file(file_path)
    
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
            if requirements[s['type']] > 0 and s['name'] not in character['Spells']
        ]

        chosen_spell = random.choice(available_pool)

        add_item(character, "Spells", chosen_spell['name'])
        requirements[chosen_spell['type']] -= 1
        learned_count += 1
        
        print(f"You have just learned the  spell: {chosen_spell['name']} ({chosen_spell['type']})")
        input("\nPress Enter to continue...")

    print("\nYou have completed your basic spell training at Hogwarts!")
    print("\nHere are the spells you now master:")

    for spell_name in character['Spells']:
            # Find the specific spell dictionary that matches the name
            spell_data = next((s for s in all_spells if s['name'] == spell_name), None)
            
            if spell_data:
                print(f"- {spell_data['name']} ({spell_data['type']}): {spell_data['description']}")

def magic_quiz(character, houses, file_path="../data/magic_quiz.json"):

    print("\nWelcome to the Hogwarts magic quiz !")
    print(f"Professor Snape: 'Let's see if you were paying attention, {character['First Name']}...'")

    quiz_data = load_file(file_path)
    score = 0
    total_questions = len(quiz_data)

    for item in quiz_data:
        question = item['question']
        options = item['options']
        correct_answer = item['answer']

        user_choice = ask_choice(question, options)

        if user_choice == correct_answer:
            print("Correct answer! +25 points for your house.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer was: {correct_answer}.'")

    points_awarded = score*25
    house_name = character.get("House")
    
    print(f"\nQuiz Finished! You got {score}/{total_questions} correct.")

    update_house_points(houses, house_name, points_awarded)

    from chapters.chapter_3 import learn_spells, magic_quiz

def start_chapter_3(character, houses):

    learn_spells(character)
    magic_quiz(character, houses)
    
    return character