import random
from utils.input_utils import ask_choice

def final_duel_basilisk(character, houses):
    print(" THE CHAMBER OF SECRETS: THE FINAL DUEL ")
    print("The cheers from the Quidditch stands still echo in your ears,\n but as you walk back to the castle, a chilling, hissing voice\n vibrates through the very walls...\n You descend deep beneath the school. Before you stands the \n massive statue of Salazar Slytherin. A heavy slithering sound \n approaches. The Basilisk has arrived!")
    print("The massive serpent lunges from the pipes. The Basilisk is here!")

    basilisk_hp = 20
    player_hp = 10
    sword_chance = 0.1
    
    while player_hp > 0 and basilisk_hp > 0:
        print(f"\n--- BATTLE STATUS ---")
        print(f"Your HP: {player_hp} | Basilisk HP: {basilisk_hp}")

        choice = ask_choice("What will you do?", ["Attack", "Dodge"])
        
        basilisk_will_attack = random.randint(1, 5) <= 2

        if choice == "Attack":
            print("You strike with your small blade! (Dealt 2 damage)")
            basilisk_hp -= 2
            if basilisk_will_attack:
                player_hp -= 5
                print("The Basilisk counter-attacks! You take 5 damage.")
                
        elif choice == "Dodge":
            print("You dive out of the way!")
            if basilisk_will_attack:
                print("The Basilisk's fangs miss you by an inch! Safe.")
            else:
                print("The Basilisk hissed, preparing its next move.")

        if player_hp <= 0:
            break

        if random.random() < sword_chance:
            print(" FAWKES DROPS THE SORTING HAT! ")
            print(" You pull the SWORD OF GRYFFINDOR from the hat! ")
            print(" With one mighty swing, you pierce the Basilisk's brain! ")
            
            basilisk_hp = 0  #<--- INSTA-KILL
        else:
            sword_chance += 0.15
            print("The sword hasn't appeared yet... stay alive!")

    if player_hp <= 0:
        print("\nYou have been defeated by the Basilisk. Hogwarts is lost...")
        return False
    else:
        print("\nThe Great Serpent lies dead at your feet!")
        house_name = character.get("House", "Gryffindor")
        houses[house_name] += 200 
        print(f"Congratulations! 200 points awarded to {house_name}!")
        return True